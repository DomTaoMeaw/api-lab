
import requests

def test_get_tools():
    headers = {"Authorization": "token abcdef0123456789"}

    response = requests.get(
        "https://quickpizza.grafana.com/api/tools",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()
    assert data["tools"] == ["Knife", "Pizza cutter", "Scissors"]
