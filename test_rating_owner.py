
def test_other_user_cannot_read_rating(api, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)

    print("Read status:", res.status_code)

    assert 400 <= res.status_code < 500


def test_other_user_cannot_update_rating(api, rating, other_auth, auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(
        path,
        json={"stars": 5},
        headers=other_auth,
    )

    print("Update status:", res.status_code)

    assert 400 <= res.status_code < 500

    check = api.get(path, headers=auth)
    assert check.status_code == 200
    assert check.json()["stars"] == rating["stars"]


def test_other_user_cannot_delete_rating(api, rating, other_auth, auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)

    print("Delete status:", res.status_code)

    assert 400 <= res.status_code < 500

    check = api.get(path, headers=auth)
    assert check.status_code == 200
    assert check.json() == rating
