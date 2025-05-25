from typing import List
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Dummy marks database
marks_db = {
    "X": 10,
    "Y": 20,
    "Alice": 85,
    "Bob": 92,
    "Charlie": 75,
}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    result = [marks_db.get(n, 0) for n in name]
    return JSONResponse(content={"marks": result})
