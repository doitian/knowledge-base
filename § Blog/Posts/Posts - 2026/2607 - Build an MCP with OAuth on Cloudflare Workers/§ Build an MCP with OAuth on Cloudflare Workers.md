---
date: '2026-07-24T19:48:12+0800'
draft: false
aliases: ["Build an MCP with OAuth on Cloudflare Workers"]
tags:
  - api
  - automation
  - javascript
  - security
  - tool
description: "Wrap an IFTTT webhook as an MCP on Cloudflare Workers, protect it with Cloudflare Access OAuth, and create Google Tasks without a Workspace license or exposed secrets."
---

# Build an MCP with OAuth on Cloudflare Workers

**Status**:: #i
**Zettel**:: #zettel/permanent
**Created**:: [[2026-07-24]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/07/build-an-mcp-with-oauth-on-cloudflare-workers/)

I wanted MCP clients to create Google Tasks for me. The Google Tasks API is gated behind a business license I don't have. IFTTT already bridges webhooks to Google Tasks—but a Maker webhook URL is a bearer secret. Putting that key in local MCP config is a bad idea.

<!--more-->

The fix is a thin Cloudflare Worker plus **Cloudflare Access Managed OAuth**:

1. Worker holds the IFTTT key as a secret and speaks MCP over HTTP
2. Access sits in front, handles OAuth login with your IdP
3. Worker verifies the Access JWT (`Cf-Access-Jwt-Assertion`) before running tools

The full example: [doitian/google-task-ifttt-webhook-mcp](https://github.com/doitian/google-task-ifttt-webhook-mcp). Most of it was scaffolded by AI; the interesting part is the shape, not the TypeScript.

## The problem

| Piece | Constraint |
| ------- | ------------ |
| Google Tasks API | Needs a Workspace-style setup I don't want to pay for |
| IFTTT Maker webhook | Works, but the URL *is* the credential |
| MCP clients | Expect remote HTTP tools with OAuth |

```
MCP Client
  → Cloudflare Access (OAuth)
  → Worker (JWT)
  → IFTTT
  → Google Tasks
```

Clients never see `IFTTT_MAKER_TASK_KEY`. They only hold a short-lived Access token after login.

## IFTTT side

One applet:

- **If**: Maker Webhooks → Receive a web request, event name `task`
- **Then**: Google Tasks → Create a task (title / notes / due from the payload)

The Worker posts to:

```
https://maker.ifttt.com/trigger/task/json/with/key/{KEY}
```

with `{ "title", "notes?", "due?" }`. The key never leaves Cloudflare.

## Three secrets

```pwsh
npx wrangler secret put IFTTT_MAKER_TASK_KEY
npx wrangler secret put CF_ACCESS_TEAM_DOMAIN
npx wrangler secret put CF_ACCESS_AUD
```

| Secret | Role |
| -------- | ------ |
| `IFTTT_MAKER_TASK_KEY` | Maker webhook key |
| `CF_ACCESS_TEAM_DOMAIN` | Zero Trust team domain (e.g. `myteam.cloudflareaccess.com`) |
| `CF_ACCESS_AUD` | Access application audience tag (validates JWT `aud`) |

No custom authorize page, no signing keys you mint yourself. Access is the authorization server.

## Cloudflare Access

In the [Zero Trust dashboard](https://one.dash.cloudflare.com/):

1. **Access** → **Applications** → **Add** → **Self-hosted**
2. Point the app at your Worker hostname (`*.workers.dev` or a custom domain)
3. Pick an IdP (Google, GitHub, email OTP, …) and an allow policy for yourself
4. Enable **Managed OAuth (Beta)** — this is what MCP clients need for the OAuth dance
5. Copy the team domain and Application Audience (AUD)

Access issues JWTs; MCP clients send them as `Cf-Access-Jwt-Assertion`. The Worker verifies with the team's JWKS:

```ts
const JWKS = createRemoteJWKSet(
  new URL(`${issuer}/cdn-cgi/access/certs`),
);
await jwtVerify(token, JWKS, {
  issuer,
  ...(env.CF_ACCESS_AUD ? { audience: env.CF_ACCESS_AUD } : {}),
});
```

(`jose` on Workers with `nodejs_compat`.)

## Worker: just MCP + verify

Business logic is tiny:

- `POST /` or `POST /mcp` — JSON-RPC (`initialize`, `tools/list`, `tools/call`)
- One tool: `create_google_task` (`title` required; `notes`, `due` optional)
- Reject anything without a valid Access JWT

No OAuth endpoints in the Worker. Access owns login; the Worker only checks the assertion header.

## Client config

Point the client at the Worker URL and enable OAuth. Example shape (keys vary by client):

```json
{
  "mcp": {
    "google-tasks": {
      "type": "remote",
      "url": "https://google-task-mcp.yourdomain.com"
    }
  }
}
```

The client discovers OAuth via Access, opens the browser for your IdP, then attaches the Access JWT on MCP calls.

## Why this shape works with AI

The task decomposes cleanly:

1. **MCP handler** — fixed JSON-RPC + one tool schema
2. **IFTTT `fetch`** — secret from `env`
3. **Access JWT verify** — JWKS + `aud`
4. **Wrangler secrets** — nothing in git

Describe the constraints ("don't expose the IFTTT URL", "Cloudflare Access OAuth", "Worker MCP") and get a deployable skeleton. Review JWT verification and secret handling; treat the tool body as glue.

## Takeaways

- Skip the official Tasks API if IFTTT already has the integration.
- Keep Maker keys in Worker secrets, not client config.
- Cloudflare Access Managed OAuth turns IdP login into MCP-friendly OAuth without rolling your own authorize/token endpoints.
- The Worker only needs to verify `Cf-Access-Jwt-Assertion` and call IFTTT.

Source: [github.com/doitian/google-task-ifttt-webhook-mcp](https://github.com/doitian/google-task-ifttt-webhook-mcp).
