import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from fastapi.testclient import TestClient
from yourtool.api import app


def test_scan_endpoint_returns_json():
    client = TestClient(app)
    response = client.post("/scan", json={"target": "example.com"})
    assert response.status_code == 200
    assert response.json()["target"] == "example.com"
