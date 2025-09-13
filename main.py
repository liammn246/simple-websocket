import json
from pyexpat.errors import messages

from fastapi import  FastAPI, WebSocket, WebSocketDisconnect
from manager import ConnectionManager
app = FastAPI()
manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_connection(websocket: WebSocket):
    await websocket.accept()
    json_username = await websocket.receive_text()
    username = json.loads(json_username)['username']
    await manager.accept(websocket, username)
    try:
        while True:
            json_message = await websocket.receive_text()
            message = json.loads(json_message)['message']
            await manager.user_broadcast(websocket, message)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        