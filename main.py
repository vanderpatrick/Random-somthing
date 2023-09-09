from fastapi import FastAPI
from uvicorn import run
from router import router
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append("/Users/chief/PycharmProjects/MyBalance")
app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
    run(
        "main:app",
        reload=True,
        host="127.0.0.1",
        port=8000,
        access_log=True,
    )


if __name__ == "__main__":
    main()
