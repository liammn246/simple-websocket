from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.connections: dict[WebSocket:str] = {}

    async def accept(self, websocket: WebSocket, username: str):
        self.connections[websocket] = username

    async def user_broadcast(self, websocket: WebSocket, message: str):
        user_message = self.connections[websocket]+': '+message
        for user in self.connections:
            await user.send_text(user_message)
    
    async def server_broadcast(self, message: str):
        for user in self.connections:
            await user.send_text(message)

    async def disconnect(self, websocket: WebSocket):
        disconnected_user = self.connections.pop(websocket)
        await self.server_broadcast("~~ "+disconnected_user+" has left. ~~")
        