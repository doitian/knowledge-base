---
date: 2017-10-22
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2017-10-22


- [Vim After 15 Years | Ian Langworth’s Things of Variable Interest](https://statico.github.io/vim3.html)

    Vim tips

- [How does Ethereum work, anyway? – Preethi Kasireddy – Medium](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369)

    Introduction to Ethereum

- [Use luarocks installed via Homebrew without sudo](https://gist.github.com/doitian/8152980b4552e52f683fb6f84472d6ac)

    Edit `/usr/local/Cellar/lua@5.3/5.3.4/libexec/share/lua/5.3/luarocks/fs/lua.lua`.

    In function `fs_lua.check_command_permissions(flags)`, Change the if condition to

    ```
    if fs.exists(dir) and not fs.is_writable(dir) and not fs.is_writable(dir .. "/bin") then
    ```

## Projects 

- [fastify/fastify: Fast and low overhead web framework, for Node.js](https://github.com/fastify/fastify)

    Node.js http server using async/await.

- [ansible/awx: AWX Project](https://github.com/ansible/awx)

    Opensource Ansible Tower

- [cloudnativelabs/kube-router: A distributed load balancer, firewall and router designed for Kubernetes](https://github.com/cloudnativelabs/kube-router)

- [sheerun/vim-polyglot: A solid language pack for Vim.](https://github.com/sheerun/vim-polyglot)

- [Microsoft/napajs: Napa.js: a multi-threaded JavaScript runtime](https://github.com/Microsoft/napajs)

