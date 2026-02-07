from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/work")
def work():
    return {"result": "work completed"}

@app.get("/fail")
def fail():
    if random.random() > 0.5:
        raise Exception("simulated failure")
    return {"status": "ok"}
