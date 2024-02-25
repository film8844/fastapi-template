from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.example import router as example_router
import os


app = FastAPI(
    title=os.environ.get("TITLE"),
    description=os.environ.get("DESCRIPTION"),
    version=os.environ.get("VERSION"),
    terms_of_service=None,
    contact=None,
    license_info=None,
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router)
# app.include_router(example1_router)
# app.include_router(example2_router)


@app.get("/status")
async def healthcheck() -> dict:
    return {"status": "OK"}


@app.get("/")
async def info() -> dict:
    return {"status": "OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
