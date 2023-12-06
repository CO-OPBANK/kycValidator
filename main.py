from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from routers import ocr , liveness

# FastAPI
app = FastAPI(
    title="CO-OP Bank KYC Validator",
    description="""Visit port 8088/docs for the FastAPI documentation.""",
    version="0.0.2",
)

# Configure CORS
origins = [
    "http://localhost:3000",  # Replace with the origin of your React app
    # "https://yourproductionapp.com",  # Add production origin if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
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
