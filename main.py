from fastapi import FastAPI, WebSocket
from routers import ocr , liveness

# FastAPI
app = FastAPI(
    title="CO-OP Bank KYC Validator",
    description="""Visit port 8088/docs for the FastAPI documentation.""",
    version="0.0.2",
)

app.include_router(ocr.router)
app.include_router(liveness.router)


@app.get("/")
async def root():
    return {"message": "CO-OP Bank KYC Validator"}


@app.websocket("/ws")
async def health_check(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_json({"msg":data})
