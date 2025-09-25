# test_app.py
from app import app  # calls the app in question for testing

def test_about_returns_200_and_json():
    # tests the first endpoint of my API
    client = app.test_client()
    resp = client.get("/about")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "name" in data

