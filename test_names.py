
import requests

def test_get_pizza_names():
    response = requests.get("https://quickpizza.grafana.com/api/names")

    assert response.status_code == 200

    data = response.json()
    assert "Margherita" in data["names"]
