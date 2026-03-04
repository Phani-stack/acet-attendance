from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://attendance.sandyy.in"

@app.post("/api/attendance")
def get_attendance(
    username: str = Form(...),
    campus: str = Form("ACET")   
):
    session = requests.Session()

    session.post(f"{BASE_URL}/get-attendance", data={
        "campus": campus,
        "username": username
    })

    response = session.get(f"{BASE_URL}/api/get-attendance-table/entire")

    if response.status_code != 200:
        return JSONResponse({"error": "Failed to fetch attendance"}, status_code=400)

    return response.json()