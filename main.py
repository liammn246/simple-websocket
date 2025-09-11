from fastapi import  FastAPI, WebSocket, WebSocketDisconnect, Query
from manager import ConnectionManager
app = FastAPI()
manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_connection(websocket: WebSocket):
    await manager.accept(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("User left")


