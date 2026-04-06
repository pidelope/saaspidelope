import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.business_slug = self.scope['url_route']['kwargs']['business_slug']
        self.room_group_name = f'orders_{self.business_slug}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group (triggered by views)
    async def order_update(self, event):
        # Send a signal to HTMX via WebSocket
        # We just need to tell HTMX to refresh the monitor
        await self.send(text_data=json.dumps({
            'type': 'order_update',
            'message': 'Un nuevo pedido o cambio de estado ha ocurrido.'
        }))
