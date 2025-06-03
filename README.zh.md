# ComfyUI-Heartbeat

这是一个用于 ComfyUI 的心跳上报插件，可定期向指定网关地址发送包含本机系统状态的心跳请求，并支持多种鉴权方式。

## 功能特性

- ✅ 自动定时发送心跳包
- ✅ 携带本机系统信息（操作系统、GPU、内存等）
- ✅ 支持 Basic Auth 和 Bearer Token 鉴权
- ✅ node 地址可自定义（默认为 `http://localhost:8188`）
- ✅ 多语言支持（中文 / 英文 / 日文 自动适配）
- ✅ 提供可视化 Web UI 配置界面
- ✅ 所有配置自动持久化保存

## 安装方法

1. 将本插件文件夹复制到 ComfyUI 的 `custom_nodes` 目录下：
   ```
   cp -r ComfyUI-Heartbeat path/to/ComfyUI/custom_nodes/
   ```

2. 重启 ComfyUI

3. 打开设置页面进行配置

> 设置入口位置：顶部菜单栏 → Extra → Settings → Heartbeat Plugin Settings

## 配置文件存储位置

插件将配置保存在用户目录下：

```
<USER_DATA_DIR>/comfyui-heartbeat.json
```
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
## 心跳包示例（POST Body）

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

## 协议

MIT
