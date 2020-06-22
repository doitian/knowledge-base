# Podman

⚡ Proxy

```
unqualified-search-registries = ['docker.io']

[[registry]]
prefix = "docker.io"
location = "docker.io"

[[registry.mirror]]
prefix = "docker.io"
location = "docker.mirrors.ustc.edu.cn"
```

⚡ Allow mounting local folder

```
--security-opt label=disable
```
