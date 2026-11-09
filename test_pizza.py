
import requests

BASE_URL = "https://quickpizza.grafana.com"
AUTH = {"Authorization": "token abcdef0123456789"}


def test_create_vegetarian_pizza():
    body = {"mustBeVegetarian": True}

    response = requests.post(
        BASE_URL + "/api/pizza",
        headers=AUTH,
        json=body
    )

    assert response.status_code == 200

    data = response.json()

    assert data["pizza"]["name"] != ""
    assert data["vegetarian"] is True

    for ingredient in data["pizza"]["ingredients"]:
        assert ingredient["vegetarian"] is True


def test_create_pizza_without_token():
    body = {"mustBeVegetarian": True}

    response = requests.post(
        BASE_URL + "/api/pizza",
        json=body
    )

    assert response.status_code == 401
    assert response.json() == {"error": "authentication failed"}
