import os

from glide import (
    GlideClientConfiguration,
    GlideClient,
    NodeAddress,
    Logger,
    LogLevel,
    RequestError,
    ClosingError
)


class ValkeyRepository:
    Logger.set_logger_config(LogLevel.INFO)

    client = None

    def __init__(self):
        self.host = os.getenv('VALKEY_HOST', '127.0.0.1')
        self.port = 6379

    async def open(self):
        addresses = [
            NodeAddress(self.host, self.port),
        ]
        config = GlideClientConfiguration(addresses=addresses, use_tls=True)
        try:
            self.client = await GlideClient.create(config)
        except (TimeoutError, RequestError, ConnectionError, ClosingError) as ex:
            print(f'Valkey Client Open Error: {ex}')

    async def ping(self):
        return await self.client.ping()

    async def close(self):
        await self.client.close()

    def __del__(self):
        self.close()
