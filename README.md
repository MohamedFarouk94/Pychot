# Pychot 🧠💬

**Pychot** is a secure and lightweight chat server and client application built with Django, Django Channels, Redis, and Tkinter. It features real-time messaging, authentication, and chat history management.

---

## 🔧 Features

- 🧑‍💻 Django backend for handling users, rooms, and chat messages
- ⚡ WebSocket support via Django Channels
- 🧠 SQLite3 for relational data, Redis for real-time messaging and persistence
- 🪟 Tkinter-based client GUI
- 🔐 Login system using cookies and session tokens

---

## 🗂 Project Structure

```
Pychot-master/
├── client/                # Python client (GUI + REST/WebSocket)
│   ├── gui.py             # Main GUI for the chat app
│   ├── auth.py            # Handles login/authentication
│   ├── comm.py            # WebSocket communications
│   └── *.py               # Additional client logic
├── pychot/                # Django backend
│   ├── manage.py
│   ├── database/          # Django app for chat models
│   └── pychot/            # Django project settings
├── dump.rdb               # Redis persistence file
├── cookies.txt            # Session cookies (for client login)
└── .gitignore
```

---

## 🚀 Getting Started

### Backend (Django + Redis)

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run Redis server (make sure `redis-server` is installed):
    ```bash
    redis-server
    ```

3. Run Django server:
    ```bash
    cd pychot
    python manage.py migrate
    python manage.py runserver
    ```

4. Run Daphne server (for WebSockets):
    ```bash
    daphne pychot.asgi:application
    ```

---

### Client (Tkinter)

1. From the project root:
    ```bash
    python3 client/gui.py <username> <password>
    ```

---

## 🛡 Authentication

- Users log in using username/password.
- Session cookies are saved in `cookies.txt`.
- Only logged-in users can join rooms or send/receive messages.

---

## 🗃 Chat History

- Chat messages are stored in Redis and Django DB.
- History can be fetched via REST API.

---

## 📜 License

MIT License
