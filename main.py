from typing import Dict
from fastapi import FastAPI
from util.cd import deploy

app = FastAPI()

@app.post("/event")
def event_received(event: Dict):
    deploy()