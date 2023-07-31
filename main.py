from fastapi import FastAPI
from routers import ocr

# FastAPI
app = FastAPI(
    title="CO-OP Bank KYC Validator",
    description="""Visit port 8088/docs for the FastAPI documentation.""",
    version="0.0.2",
)

app.include_router(ocr.router)


@app.get("/")
async def root():
    return {"message": "CO-OP Bank KYC Validator"}

