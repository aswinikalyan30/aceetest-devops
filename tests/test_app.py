import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_html(client):
    response = client.get("/")
    assert b"<html>" in response.data or b"<!DOCTYPE html>" in response.data.lower() or b"ACEest" in response.data


def test_add_client_redirects(client):
    response = client.post("/add_client", data={
        "name": "John Doe",
        "age": "30",
        "height": "180",
        "weight": "80",
        "program": "Weight Loss"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/"


def test_add_client_appears_in_list(client):
    client.post("/add_client", data={
        "name": "Jane Smith",
        "age": "25",
        "height": "165",
        "weight": "60",
        "program": "Muscle Gain"
    })
    response = client.get("/")
    assert b"Jane Smith" in response.data


def test_add_workout_redirects(client):
    response = client.post("/add_workout", data={
        "client": "John Doe",
        "date": "2026-03-10",
        "workout": "Cardio",
        "duration": "45"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/"


def test_add_multiple_clients(client):
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        client.post("/add_client", data={
            "name": name,
            "age": "28",
            "height": "170",
            "weight": "70",
            "program": "Endurance"
        })
    response = client.get("/")
    for name in names:
        assert name.encode() in response.data


def test_invalid_route_returns_404(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404