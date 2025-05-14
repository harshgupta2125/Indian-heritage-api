import json
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="India Cultural Heritage API", version="1.0")

# --- Data Models ---
class HistoricalSite(BaseModel):
    id: int
    name: str
    location: str
    state: str
    description: str
    established_year: int

class CulturalEvent(BaseModel):
    id: int
    title: str
    date: str
    state: str
    location: str
    description: str

class LocalTradition(BaseModel):
    id: int
    name: str
    state: str
    summary: str

# --- In-Memory Storage (Loaded from JSON Files) ---
with open("data/historical_sites.json") as f:
    historical_sites = [HistoricalSite(**item) for item in json.load(f)]

with open("data/cultural_events.json") as f:
    cultural_events = [CulturalEvent(**item) for item in json.load(f)]

with open("data/local_traditions.json") as f:
    local_traditions = [LocalTradition(**item) for item in json.load(f)]


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>India Cultural Heritage API</title>
        </head>
        <body style="font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4;">
            <div style="background-color:gray; width:980px; height:500px; padding:50px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.5); margin: 0 auto;">
                <h1> Welcome to the India Cultural Heritage API</h1>
                <p>This API provides structured information about India's rich cultural heritage including historical sites, cultural events, and local traditions.</p>
                
                <h2>📚 Available Endpoints</h2>
                <ul>
                    <li><strong>/sites/</strong> – Get all historical heritage sites</li>
                    <li><strong>/events/</strong> – Get all cultural events across Indian states</li>
                    <li><strong>/traditions/</strong> – Discover local traditions and folk practices</li>
                    <li><strong>/docs</strong> – Swagger UI for testing and exploring the API</li>
                    <li><strong>/redoc</strong> – ReDoc API documentation view</li>
                </ul>

                <hr />
                <footer>
                    <p style="font-size: 18px; color: black;">Created by <strong>[Harsh Gupta] </strong></p>
                </footer>
            </div>
        </body>
    </html>
    """


@app.get("/sites/", response_model=List[HistoricalSite])
def get_sites(state: str = None):
    if state:
        return [s for s in historical_sites if s.state.lower() == state.lower()]
    return historical_sites

@app.get("/events/", response_model=List[CulturalEvent])
def get_events(state: str = None):
    if state:
        return [e for e in cultural_events if e.state.lower() == state.lower()]
    return cultural_events

@app.get("/traditions/", response_model=List[LocalTradition])
def get_traditions(state: str = None):
    if state:
        return [t for t in local_traditions if t.state.lower() == state.lower()]
    return local_traditions

# --- POST Endpoints ---
@app.post("/sites/", response_model=HistoricalSite)
def create_site(site: HistoricalSite):
    historical_sites.append(site)
    return site

@app.post("/events/", response_model=CulturalEvent)
def create_event(event: CulturalEvent):
    cultural_events.append(event)
    return event

@app.post("/traditions/", response_model=LocalTradition)
def create_tradition(tradition: LocalTradition):
    local_traditions.append(tradition)
    return tradition
