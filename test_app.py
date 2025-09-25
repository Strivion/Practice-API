# test_app.py
from app import app  # rename 'app' to your module name if needed

def test_about_returns_200_and_json():
    client = app.test_client()
    resp = client.get("/about")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "name" in data
