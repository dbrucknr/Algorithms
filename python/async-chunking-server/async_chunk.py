import aiohttp
import asyncio
from typing import List

async def post_data_to_api(data: List[str], api_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json={
            "data": data
        }) as response:
            return await response.json()

async def chunked_data_queue(data: List[str], api_url: str, chunk_size: int):
    queue = asyncio.Queue()

    # Enqueue the data in chunks
    for i in range(0, len(data), chunk_size):
        await queue.put(data[i:i+chunk_size])

    # Signal the end of the queue
    await queue.put(None)

    # Send the chunks to the API asynchronously
    async def send_data():
        while True:
            chunk = await queue.get()
            if chunk is None:
                break
            await post_data_to_api(chunk, api_url)

    # Start the send_data tasks
    await asyncio.gather(*[asyncio.create_task(send_data()) for _ in range(5)])
    
# Usage example
data = list(range(10000))
api_url = "http://localhost:8000"
chunk_size = 5
asyncio.run(chunked_data_queue(data, api_url, chunk_size))
