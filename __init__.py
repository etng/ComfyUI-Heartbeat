from .heartbeat import start_heartbeat_task
from aiohttp import web
from .config_loader import load_config, save_config
print("🔌 Heartbeat plugin loaded")

routes = web.RouteTableDef()

@routes.post("/custom_nodes/ComfyUI-Heartbeat/save_config")
async def save_config_handler(request):
    data = await request.json()
    save_config(data)
    return web.Response(text="OK")

@routes.get("/custom_nodes/ComfyUI-Heartbeat/get_config")
async def get_config_handler(request):
    data = load_config()
    return web.json_response(data)

def start_heartbeat_task():
    from .heartbeat import start_heartbeat_task as real_start
    real_start(routes)

start_heartbeat_task()

WEB_DIRECTORY = "./web"
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
