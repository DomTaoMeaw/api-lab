import pytest


@pytest.mark.parametrize("excluded", [["Knife"], ["Scissors"]])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.parametrize(
    "excluded",
    [
        [],
        ["Knife"],
        ["Knife", "Scissors"],
    ],
)
def test_excluded_tools_count(api, auth, excluded):
    body = {"excludedTools": excluded}

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.xfail(
    reason="Defect 1: API returns HTTP 500 instead of HTTP 400",
    strict=True,
)
def test_exclude_all_tools(api, auth):
    body = {
        "excludedTools": ["Knife", "Scissors", "Pizza cutter"]
    }

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": "no available tools"}