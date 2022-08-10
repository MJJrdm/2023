import os
# import channels.asgi

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game.settings")
# channel_layer = channels.asgi.get_channel_layer()

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_puzzle_a_day.settings')
# channel_layer = channels.asgi.get_channel_layer()
application = get_asgi_application()