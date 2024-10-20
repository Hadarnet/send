import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import telecom.routing
import telecom.middleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": telecom.middleware.QueryAuthMiddleware(
        URLRouter(
            telecom.routing.websocket_urlpatterns
        )
    ),
})