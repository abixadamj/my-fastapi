import os
import uvicorn
from fastapi import FastAPI
from datetime import datetime

app: FastAPI = FastAPI()
__PORT__ = os.getenv("APP_PORT", 5501)
__APP_TYPE__ = os.getenv("APP_TYPE", None)


@app.get("/")
def main():
    return {"os": os.uname(),
            "Made by:": "Adam Jurkiewicz",
            "Current date/time:": str(datetime.now()),
            }


if __name__ == "__main__":
    print(f"Start APP {__APP_TYPE__} on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))
