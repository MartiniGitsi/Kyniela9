from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}


@app.get("/ping")
def ping():
    return {"ping": "pong"}
