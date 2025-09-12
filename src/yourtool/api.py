from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .core import run_scan


class ScanRequest(BaseModel):
    """Request body for scan endpoint."""

    target: str


class ScanResult(BaseModel):
    """Result of a scan operation."""

    status: str
    target: str


app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/scan", response_model=ScanResult)
def scan_endpoint(request: ScanRequest) -> ScanResult:
    """Run a scan on the provided target."""
    result = run_scan(request.target)
    return ScanResult(**result)
