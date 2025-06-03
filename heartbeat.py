import asyncio
import requests
import logging
import comfy
import sys
import comfy.model_management
from comfyui_version import __version__
import os
import server
from .config_loader import load_config,save_config
logger = logging.getLogger("ComfyUI")
def SystemStats():
    device = comfy.model_management.get_torch_device()
    device_name = comfy.model_management.get_torch_device_name(device)
    cpu_device = comfy.model_management.torch.device("cpu")
    ram_total = comfy.model_management.get_total_memory(cpu_device)
    ram_free = comfy.model_management.get_free_memory(cpu_device)
    vram_total, torch_vram_total = comfy.model_management.get_total_memory(device, torch_total_too=True)
    vram_free, torch_vram_free = comfy.model_management.get_free_memory(device, torch_free_too=True)

    system_stats = {
        "system": {
            "os": os.name,
            "ram_total": ram_total,
            "ram_free": ram_free,
            "comfyui_version": __version__,
            "python_version": sys.version,
            "pytorch_version": comfy.model_management.torch_version,
            "embedded_python": os.path.split(os.path.split(sys.executable)[0])[1] == "python_embeded",
            "argv": sys.argv
        },
        "devices": [
            {
                "name": device_name,
                "type": device.type,
                "index": device.index,
                "vram_total": vram_total,
                "vram_free": vram_free,
                "torch_vram_total": torch_vram_total,
                "torch_vram_free": torch_vram_free,
            }
        ]
    }
    return system_stats
 
async def heartbeat_task():
    while True:
        config = load_config()
        gateway_url = config.get("gateway_url")
        node_url = config.get("node_url", "http://localhost:8188")
        auth_type = config.get("auth_type", "none")
        # logging.debug(f"heartbeat config is {repr(config)}")
        if not gateway_url:
            await asyncio.sleep(5)
            continue

        headers = {}
        auth = None

        if auth_type == "basic":
            from requests.auth import HTTPBasicAuth
            auth = HTTPBasicAuth(
                config["basic_username"],
                config["basic_password"]
            )
        elif auth_type == "bearer":
            headers["Authorization"] = f"Bearer {config['bearer_token']}"

        data = {
            "node_url": node_url,
            "status": "alive",
            "system_info": SystemStats()
        }

        try:
            response = requests.post(gateway_url, json=data, headers=headers, auth=auth, timeout=5)
            logger.info(f"Heartbeat sent to {gateway_url}, status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Failed to send heartbeat: {e}")

        await asyncio.sleep(config.get("heartbeat_interval", 30))




def start_heartbeat_task(routes):
    instance = server.PromptServer.instance

    if instance:
        logger.info("🔌 Starting background heartbeat task...")
        instance.loop.create_task(heartbeat_task())
        instance.app.add_routes(routes)
    else:
        logger.warning("⚠️ Could not get server instance to schedule heartbeat.")
 