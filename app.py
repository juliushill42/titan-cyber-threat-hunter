from fastapi import FastAPI
from agent import Agent15
app = FastAPI(title="Cyber-Threat-Hunter")
agent = Agent15()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
