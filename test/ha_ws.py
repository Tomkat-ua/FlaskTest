import asyncio
import websockets
import json

HA_URL = "wss://ha2.home-pi.keenetic.pro/api/websocket"  # або твоя IP-адреса
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZTNkODQwZTljOTM0YjViODlkOWYwN2M0YmY5ZWQ0ZCIsImlhdCI6MTc1MzYyODMyNiwiZXhwIjoyMDY4OTg4MzI2fQ.6R_j1AEAtS_rweoEXCGya9ON_eADKQ4M3hi9nGm8zK4"

async def listen():
    async with websockets.connect(HA_URL) as ws:
        # Handshake
        msg = await ws.recv()
        print("Connected:", msg)
        await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))

        auth_result = await ws.recv()
        print("Auth:", auth_result)

        # Підписка на всі зміни станів
        await ws.send(json.dumps({
            "id": 1,
            "type": "subscribe_events",
            "event_type": "state_changed"
        }))

        # Обробка подій
        while True:
            msg = await ws.recv()
            event = json.loads(msg)
            entity_id = event.get("event", {}).get("data", {}).get("entity_id", "")
            new_state = event.get("event", {}).get("data", {}).get("new_state", {}).get("state", "")
            if entity_id:
                print(f"[{entity_id}] → {new_state}")

asyncio.run(listen())
