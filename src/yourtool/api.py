"""FastAPI application exposing scanning functionality."""

from fastapi import FastAPI
from pydantic import BaseModel

from . import core

app = FastAPI()


class ScanRequest(BaseModel):
    """Request model for the scan endpoint."""

    target: str


@app.post("/scan")
async def scan(request: ScanRequest):
    """Run a scan for the given target and return the result.

    Parameters
    ----------
    request: ScanRequest
        Incoming request containing the target to scan.

    Returns
    -------
    dict
        JSON serializable result produced by :func:`core.run_scan`.
    """

    return core.run_scan(request.target)
