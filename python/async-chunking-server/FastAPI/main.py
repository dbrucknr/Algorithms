from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse
from typing import List
from pydantic import BaseModel

class Data(BaseModel):
    data: List[int]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return "Main"

@app.post("/")
async def receieve(data: Data):
    print(data)
    return {
        "Receieved": data
    }

@app.get("/stream")
async def stream():
    response = StreamingResponse()
    response.content_type = "text/event-stream"
    await response.prepare(app.client.scope)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Message text was: {data}")
