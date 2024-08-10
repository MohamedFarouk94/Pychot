import requests
from urllib.parse import urljoin

DJANGO_SERVER_URL = 'http://127.0.0.1:8000/'


async def authenticate(username, password):
    login_url = urljoin(DJANGO_SERVER_URL, 'accounts/login/')
    session = requests.Session()
    response = session.get(urljoin(DJANGO_SERVER_URL, 'accounts/login/'))
    response.raise_for_status()
    csrftoken = session.cookies.get('csrftoken')

    login_response = session.post(login_url, data={
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrftoken
    })

    if login_response.status_code == 200:
        print('Login successful')
        return session.cookies.get_dict()
    else:
        print('Login failed')
        return None
