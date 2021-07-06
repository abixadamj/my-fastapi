import os
import uvicorn
from fastapi import FastAPI, Request
from datetime import datetime

app: FastAPI = FastAPI()
__PORT__ = os.getenv("APP_PORT", 5501)
__APP_TYPE__ = os.getenv("APP_TYPE", None)


@app.get("/")
async def main(request: Request):
    return {"os": os.uname(),
            "Made by:": "Adam Jurkiewicz",
            "Webpage": "https://jurkiewicz.tech",
            "E-mail": "adam@jurkiewicz.tech",
            "Current date/time on server": str(datetime.now()),
            "Want to see the source?": "Yes....",
            "Point browser to...": "https://github.com/abixadamj/my-fastapi",
            "Client's IP": request.client.host,
            }


if __name__ == "__main__":
    print(f"Start APP {__APP_TYPE__} on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))
