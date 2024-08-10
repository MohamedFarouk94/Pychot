# websocket_client/client.py
import asyncio
import websockets
import requests
from urllib.parse import urljoin

# Django server URL
DJANGO_SERVER_URL = 'http://127.0.0.1:8000/'

# WebSocket URL
WEBSOCKET_URL = 'ws://127.0.0.1:8000/ws/chat/room1/'
ECHOURL = 'ws://127.0.0.1:8000/ws/echo/'

# User credentials
USERNAME = 'user1'
PASSWORD = 'password-1'


async def authenticate():
    login_url = urljoin(DJANGO_SERVER_URL, 'accounts/login/')
    session = requests.Session()
    response = session.get('http://127.0.0.1:8000/accounts/login/')
    response.raise_for_status()
    csrftoken = session.cookies.get('csrftoken')

    # Login to the Django server
    login_response = session.post(login_url, data={
        'username': USERNAME,
        'password': PASSWORD,
        'csrfmiddlewaretoken': csrftoken
    })

    if login_response.status_code == 200:
        print('Login successful')
        return session.cookies.get_dict()
    else:
        print('Login failed')
        return None


async def send_message(cookie_header):
    async with websockets.connect(WEBSOCKET_URL, extra_headers=cookie_header) as websocket:
        message = input('Enter your message: ')
        await websocket.send(message)
        print(f'Sent: {message}')

        response = await websocket.recv()
        print(f'Received: {response}')


async def main():
    cookies = await authenticate()
    if cookies:
        cookie_header = {
            'Cookie': '; '.join([f'{name}={value}' for name, value in cookies.items()])
        }
        await send_message(cookie_header)


if __name__ == '__main__':
    asyncio.run(main())
