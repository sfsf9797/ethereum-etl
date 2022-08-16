
import asyncio
from web3 import WebsocketProvider
# Mostly copied from web3.py/providers/websocket.py. Supports batch requests.
class BatchWebSocketProvider(WebsocketProvider):

    def make_batch_request(self, text):
        self.logger.debug("Making request Websocket. URI: %s, Request: %s",
                          self.endpoint_uri, text)
        request_data = text.encode('utf-8')
        future = asyncio.run_coroutine_threadsafe(
            self.coro_make_request(request_data), WebsocketProvider._loop
        )
        self.logger.debug("Getting response Websocket. URI: %s, "
                          "Request: %s, Response: %s",
                          self.endpoint_uri, text, future.result())
        return future.result()
        
