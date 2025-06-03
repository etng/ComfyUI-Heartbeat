# ComfyUI-Heartbeat

A plugin for ComfyUI that sends periodic heartbeat requests to a configured gateway, including system information and node status.

## Features

- ✅ Periodic heartbeat requests
- ✅ Includes system info (OS, GPU, RAM)
- ✅ Supports Basic Auth / Bearer Token
- ✅ Node URL configurable
- ✅ Multilingual support (en/zh/ja)
- ✅ Web UI configuration panel
- ✅ Config saved in user directory

## Installation

1. Copy this folder into your `custom_nodes` directory:
   ```
   cp -r ComfyUI-Heartbeat path/to/ComfyUI/custom_nodes/
   ```

2. Restart ComfyUI

3. Open Settings > "Heartbeat Plugin Settings" to configure

## Configuration File

The plugin saves its configuration in:

```
<USER_DATA_DIR>/comfyui-heartbeat.json
```

Example:

```json
{
  "gateway_url": "http://your-gateway.com/heartbeat",
  "node_url": "http://localhost:8188",
  "auth_type": "none",
  "heartbeat_interval": 30
}
```

```json
{
    "gateway_url": "http://localhost:9999",
    "node_url": "http://localhost:8188",
    "auth_type": "bearer",
    "bearer_token": "12345",
    "heartbeat_interval": 30
}
```

```json
{
    "gateway_url": "http://localhost:9999",
    "node_url": "http://localhost:8188",
    "auth_type": "basic",
    "basic_username": "hello",
    "basic_password": "world",
    "heartbeat_interval": 30
}
```

## Heartbeat Payload Example

```json
{
  "node_url": "http://localhost:8188",
  "status": "alive",
  "system_info": {
    "os": "Linux",
    "ram": "64GB",
    "device": "cuda",
    ...
  }
}
```

## License

MIT
