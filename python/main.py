import json
import os.path

from fastapi import FastAPI
from starlette.websockets import WebSocket

app = FastAPI()
path = "./"
@app.websocket("/upload")
async def uploadFile(websocket: WebSocket):

    await websocket.accept()
    file = None
    dataFile = b""
    while True:
        line = await websocket.receive()
        if "text" in line:
            data = json.loads(line["text"])
            print(data["done"])
            if not data["done"]:
                d = path+data["name"]
                if os.path.exists(d):
                    os.remove(d)
                file = open(d,"ab")
            else:
                file.close()
                await websocket.close()
                break
        elif "bytes" in line:
            # print(line)
            # dataFile += line["bytes"]
            try:
                # file.write(dataFile)
                file.write(line["bytes"])
                await websocket.send_text("OK")
            except:
                await websocket.send_text("FATAL")

