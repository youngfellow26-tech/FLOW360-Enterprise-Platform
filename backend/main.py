from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random, asyncio

app = FastAPI(title="FLOW360 Enterprise Intelligence")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

tenants = {
    "africa_mining_group":{"fleet":120,"production":92},
    "global_ore_corp":{"fleet":98,"production":87}
}

class Scenario(BaseModel):
    event: str
    fuel_change: float
    logistics_delay: int

@app.get("/")
def root():
    return {"platform":"FLOW360 Enterprise","status":"online"}

@app.get("/tenants")
def get_tenants():
    return tenants

@app.get("/ai/risk/{asset}")
def risk(asset: str):
    r = round(random.uniform(0,1),2)
    return {
        "asset": asset,
        "risk_score": r,
        "status": "critical" if r > 0.7 else "stable"
    }

@app.post("/simulate")
def simulate(s: Scenario):
    return {
        "event": s.event,
        "production_impact": round(random.uniform(5,20),2),
        "fuel_change": s.fuel_change,
        "delay_days": s.logistics_delay
    }

@app.get("/esg")
def esg():
    return {
        "carbon_intensity": round(random.uniform(0.2,0.6),2),
        "water_use": random.randint(200,800),
        "safety_score": round(random.uniform(80,98),1)
    }

@app.websocket("/telemetry")
async def telemetry(ws: WebSocket):
    await ws.accept()
    while True:
        data = {
            "truck_id": random.randint(1,40),
            "temperature": random.randint(60,120),
            "fuel": random.randint(10,100),
            "load": random.randint(0,200)
        }
        await ws.send_json(data)
        await asyncio.sleep(2)
