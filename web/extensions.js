import { app } from "../../scripts/app.js";
const settingsList = [
  {
    id: "gateway_url",
    name: "HeatBeat Gateway Url",
    tooltip: '',
    defaultValue: '',
    type: "text"
  },
  {
    id: "node_url",
    name: "HeatBeat Node Url",
    tooltip: '',
    defaultValue: 'http://localhost:8188',
    type: "text"
  },

  {
    id: "auth_type",
    name: "HeatBeat Auth Type",
    tooltip: '',
    options: ['none', 'basic', 'bearer'],
    defaultValue: 'none',
    type: "combo"
  },

  {
    id: "basic_username",
    name: "HeatBeat Basic Auth Username",
    tooltip: '',
    defaultValue: '',
    type: "text"
  },
  {
    id: "basic_password",
    name: "HeatBeat Basic Auth Password",
    tooltip: '',
    defaultValue: '',
    type: "text"
  },
  {
    id: "bearer_token",
    name: "HeatBeat Bearer Token",
    tooltip: '',
    defaultValue: '',
    type: "text"
  },
  {
    id: "heartbeat_interval",
    name: "HeatBeat Interval",
    tooltip: '',
    defaultValue: '30',
    type: "number"
  }
];
const saveToServer = async (settingId, value) => {
  await fetch('/custom_nodes/ComfyUI-Heartbeat/save_setting', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ settingId, value })
  });
};
app.registerExtension({
  name: "ComfyUI Heartbeat",
  async setup(app) {
    settingsList.forEach(setting => {
      app.ui.settings.addSetting({
        ...setting,
        id: `heartbeat.${setting.id}`,
        onChange: (value) => saveToServer(setting.id, value)
      });
    })
  },
  aboutPageBadges: [
    {
      label: "ComfyUI Heartbeat 0.1",
      url: "https://github.com/etng/ComfyUI-Heartbeat",
      icon: "pi pi-home"
    }
  ]
});
