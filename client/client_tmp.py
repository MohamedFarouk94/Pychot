import requests

# URL of the login page
login_url = 'http://localhost:8000/accounts/login/'

# Start a session to maintain cookies
session = requests.Session()

# Get the login page to retrieve the CSRF token
response = session.post(login_url)
print(response.text)


"""
csrf_token = response.cookies['csrftoken']

# Prepare login data
login_data = {
    'username': 'your_username',
    'password': 'your_password',
    'csrfmiddlewaretoken': csrf_token,
}

# Post login data
response = session.post(login_url, data=login_data, headers={'Referer': login_url})

# Check if login was successful
if response.ok:
    print("Login successful!")
else:
    print(f"Login failed: {response.status_code}")
"""
