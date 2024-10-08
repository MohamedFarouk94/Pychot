from django.urls import re_path
from . import consumers
from .consumers import EchoConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/echo/$', EchoConsumer.as_asgi()),
]
