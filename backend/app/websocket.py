from fastapi import WebSocket
class Manager:
    def __init__(self): self.conns = []
    async def connect(self, ws: WebSocket):
        await ws.accept(); self.conns.append(ws)
    def disconnect(self, ws):
        if ws in self.conns: self.conns.remove(ws)
    async def broadcast(self, data: dict):
        for ws in list(self.conns):
            try: await ws.send_json(data)
            except Exception: self.disconnect(ws)
manager = Manager()
