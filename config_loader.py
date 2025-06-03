import os
import json
import folder_paths

CONFIG_PATH = os.path.join(folder_paths.get_user_directory(), "comfyui-heartbeat.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        default_config = {
            "gateway_url": "",
            "node_url": "http://localhost:8188",
            "auth_type": "none",
            "basic_username": "",
            "basic_password": "",
            "bearer_token": "",
            "heartbeat_interval": 30
        }
        save_config(default_config)
        return default_config
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)
