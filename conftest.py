
import pytest
import requests


class QuickPizza(requests.Session):

    def __init__(self):
        super().__init__()
        self.base_url = "https://quickpizza.grafana.com"

    def request(self, method, url, *args, **kwargs):
        url = self.base_url + url
        return super().request(method, url, *args, **kwargs)


@pytest.fixture(scope="session")
def api():
    return QuickPizza()
