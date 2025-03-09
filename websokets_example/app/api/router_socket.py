from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, Dict[int, WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: int, user_id: int):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = {}
        self.active_connections[room_id][user_id] = websocket

    def disconnect(self, room_id: int, user_id: int):
        if room_id in self.active_connections and user_id in self.active_connections[room_id]:
            del self.active_connections[room_id][user_id]
            if not self.active_connections[room_id]:
                # Удаляем комнату, если она пустая
                del self.active_connections[room_id]

    async def broadcast(self, message: str, room_id: int, sender_id: int):
        if room_id in self.active_connections:
            for user_id, connection in self.active_connections[room_id].items():
                message_with_class = {
                    "text": message,
                    "is_self": user_id == sender_id
                }
                await connection.send_json(message_with_class)

# ----------------------------------------------------------------------------------------------------------
# Конструктор класса

# self.active_connections — словарь, который хранит активные соединения, сгруппированные по комнатам (room_id).

# В каждой комнате (room_id) подключенные пользователи хранятся в виде {user_id: WebSocket}.

# connect

# Принимает WebSocket-соединение, идентификатор комнаты (room_id) и пользователя (user_id).

# Подтверждает соединение (websocket.accept()).

# Добавляет WebSocket в self.active_connections.

# disconnect

# Удаляет WebSocket пользователя из self.active_connections.

# Если в комнате не осталось пользователей, удаляет комнату.

# broadcast

# Отправляет сообщение всем пользователям в комнате.

# Дополнительно добавляет флаг is_self, чтобы клиент мог визуально выделять свои сообщения.
# ----------------------------------------------------------------------------------------------------------

manager = ConnectionManager()
router = APIRouter(prefix="/ws/chat")


@router.websocket("/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, user_id: int, username: str):
    await manager.connect(websocket, room_id, user_id)
    await manager.broadcast(f"{username} (ID: {user_id}) присоединился к чату.", room_id, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username} (ID: {user_id}): {data}", room_id, user_id)
    except WebSocketDisconnect:
        manager.disconnect(room_id, user_id)
        await manager.broadcast(f"{username} (ID: {user_id}) покинул чат.", room_id, user_id)
# ----------------------------------------------------------------------------------------------------------
# Маршрут

# Эндпоинт принимает три параметра из URL: room_id, user_id, username.

# Каждый пользователь подключается по URL /ws/chat/{room_id}/{user_id}.

# Подключение

# await manager.connect(...) — добавляет пользователя в список активных соединений.

# await manager.broadcast(...) — уведомляет всех пользователей комнаты о новом участнике.

# Прием и передача сообщений

# Бесконечный цикл (while True) слушает входящие сообщения через websocket.receive_text().

# После получения сообщения оно рассылается всем пользователям комнаты через manager.broadcast(...).

# Отключение

# Если соединение прерывается (WebSocketDisconnect), вызывается manager.disconnect(...).

# Отправляется сообщение в чат о выходе пользователя.

# ----------------------------------------------------------------------------------------------------------