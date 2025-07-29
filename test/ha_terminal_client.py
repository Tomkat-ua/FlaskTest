import asyncio
import websockets
import json
from rich.live import Live
from rich.table import Table

# 🔧 Конфігурація
HA_URL = "wss://ha2.home-pi.keenetic.pro/api/websocket"  # або локальна wss://IP:8123
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZTNkODQwZTljOTM0YjViODlkOWYwN2M0YmY5ZWQ0ZCIsImlhdCI6MTc1MzYyODMyNiwiZXhwIjoyMDY4OTg4MzI2fQ.6R_j1AEAtS_rweoEXCGya9ON_eADKQ4M3hi9nGm8zK4"

# Зберігаємо останній стан сенсорів
sensor_states = {}


def render_table():
    table = Table(title="📟 Home Assistant — Сенсори", expand=True)
    table.add_column("Entity ID", style="cyan", no_wrap=True)
    table.add_column("Стан", style="green")
    table.add_column("Опис", style="dim")

    for entity_id, data in sensor_states.items():
        state = data["state"]
        name = data["attributes"].get("friendly_name", "")
        table.add_row(entity_id, state, name)
    return table


async def listen():
    async with websockets.connect(HA_URL) as ws:
        # 1. Handshake
        await ws.recv()
        await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))
        await ws.recv()  # auth_ok

        # 2. Підписка на state_changed
        await ws.send(json.dumps({
            "id": 1,
            "type": "subscribe_events",
            "event_type": "state_changed"
        }))

        # 3. Живе оновлення
        with Live(render_table(), refresh_per_second=2) as live:
            while True:
                msg = await ws.recv()
                event = json.loads(msg)

                data = event.get("event", {}).get("data", {})
                entity_id = data.get("entity_id", "")
                new_state = data.get("new_state", {})

                # Фільтруємо тільки сенсори
                if entity_id.startswith("sensor.") and new_state:
                    sensor_states[entity_id] = {
                        "state": new_state.get("state", "?"),
                        "attributes": new_state.get("attributes", {})
                    }
                    live.update(render_table())


asyncio.run(listen())
