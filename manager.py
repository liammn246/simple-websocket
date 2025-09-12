from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.connections: dict[WebSocket:str] = {}

    async def accept(self, websocket: WebSocket, username: str):
        self.connections[websocket] = username

    async def broadcast(self, websocket: WebSocket, message: str):
        user_message = self.connections[websocket]+': '+message
        for user in self.connections:
            await user.send_text(user_message)

    def disconnect(self, websocket: WebSocket):
        self.connections.pop(websocket)