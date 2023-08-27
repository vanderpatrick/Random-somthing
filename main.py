from fastapi import FastAPI
from uvicorn import run
from router import router
import sys

sys.path.append("/Users/chief/PycharmProjects/MyBalance")
app = FastAPI()
app.include_router(router)


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
