
import pytest


# Test updating a rating with different star values.
@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_stars(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"

    original_stars = rating["stars"]

    res = api.put(
        path,
        json={"stars": stars},
        headers=auth,
    )

    assert res.status_code == expected_status

    if expected_status == 200:
        assert res.json()["stars"] == stars
    else:
        # The original rating must remain unchanged.
        check = api.get(path, headers=auth)

        assert check.status_code == 200
        assert check.json()["stars"] == original_stars
