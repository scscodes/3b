# test locally
### 1. install/config cloudflare tunnel
- free tier > zero trust > networks > tunnels
- download/install msi/run `cloudflared.exe service install <key>`
- or, run `cloudflared tunnel --url http://localhost:5000`
- copy output `url` into `set_webhook.py`
```shell
2024-11-08T02:13:02Z INF +--------------------------------------------------------------------------------------------+
2024-11-08T02:13:02Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
2024-11-08T02:13:02Z INF |  https://ourselves-holders--romance.trycloudflare.com                                      |
2024-11-08T02:13:02Z INF +--------------------------------------------------------------------------------------------+
```

### 2. config/run webhook
- update `set_webhook.py` with cloudflare url + token
- run script `python set_webhook.py`

### 3. run bot
- `python app.py`