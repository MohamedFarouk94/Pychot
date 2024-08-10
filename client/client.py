import asyncio
from auth import authenticate
from comm import communicate


# WebSocket URL
WEBSOCKET_URL = 'ws://127.0.0.1:8000/ws/chat/room1/'
ECHOURL = 'ws://127.0.0.1:8000/ws/echo/'

# User credentials
USERNAME = 'user1'
PASSWORD = 'password-1'


async def main(username, password):
    cookies = await authenticate(username, password)
    if cookies:
        cookie_header = {
            'Cookie': '; '.join([f'{name}={value}' for name, value in cookies.items()])
        }
        await communicate(cookie_header)


if __name__ == '__main__':
    asyncio.run(main(USERNAME, PASSWORD))
