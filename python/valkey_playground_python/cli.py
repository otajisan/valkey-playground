import asyncio

from valkey_playground_python.valkey_repository import ValkeyRepository


async def run():
    repo = ValkeyRepository()
    await repo.open()
    ping_response = await repo.ping()
    print(f'ping_response: {ping_response}')


def main():
    print('=== Hello Valkey! ===')
    print('see:')
    print('https://github.com/valkey-io/valkey-glide')
    print('https://github.com/valkey-io/valkey-glide/wiki/Python-wrapper')
    asyncio.run(run())
