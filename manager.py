from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def accept(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, message: str):
        for user in self.connections:
            await user.send_text(message)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)