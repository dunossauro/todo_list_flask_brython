from httpx import delete, post


def clean_test_database(base_url):
    assert delete(base_url + 'remove-users').status_code == 200
    assert delete(base_url + 'remove-todos').status_code == 200


def create_user(base_url, user, codes=[400, 201]):
    assert post(base_url + 'register-user', json=user).status_code in codes
