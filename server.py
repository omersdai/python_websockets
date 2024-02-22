import asyncio
import websockets

HOST = '0.0.0.0'
PORT = 8765

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f'Hello {name}!'

    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')

async def main():
    async with websockets.serve(hello, HOST, PORT):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
