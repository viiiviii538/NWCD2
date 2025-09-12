from fastapi import FastAPI
from pydantic import BaseModel

from .core import run_scan


class ScanRequest(BaseModel):
    target: str


app = FastAPI()


@app.post("/scan")
def scan_endpoint(request: ScanRequest) -> dict:
    """Run a scan on the provided target."""
    return run_scan(request.target)
