import websockets
import asyncio
from get import get_from_queue
from set import set_to_queue


WEBSOCKET_URL = 'ws://127.0.0.1:8000/ws/chat/room1/'


async def send_messages(websocket):
    while True:
        message = await get_from_queue()
        await websocket.send(message)
        # print(message)


async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        # print(response)
        set_to_queue(response)


async def communicate(cookie_header):
    async with websockets.connect(WEBSOCKET_URL, extra_headers=cookie_header) as websocket:
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))

        await asyncio.gather(send_task, receive_task)
