# tarsnap

#backup #security

⚡ SSH Tunnel

In the isolated host, edit hosts:

```
127.0.0.1 localhost v1-0-0-server.tarsnap.com
```

In the connected host, ssh into isolated host with port forwarding:

```
ssh -R 9279:v1-0-0-server.tarsnap.com:9279 isolated-host
```
