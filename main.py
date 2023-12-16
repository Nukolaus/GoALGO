import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from src.app import create_app
from src.trader.bot import run_bots

app = create_app()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origins
    allow_credentials=True,
    allow_methods=["*"],  # Set this to the allowed HTTP methods
    allow_headers=["*"],  # Set this to the allowed headers
)

@app.on_event("startup")
async def startup_event():
    asyncio.gather(run_bots())


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=9999, host="0.0.0.0")

