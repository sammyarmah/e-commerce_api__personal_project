def test_register_user(client):
    response = client.post(
        "/users",
        json = {
            "name": "Samuel",
            "email": "samuelarmah@gmail.com",
            "password": "saarmah002",
            "role": "customer"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Samuel"
    assert data["email"] == "samuelarmah@gmail.com"
    assert data["password"] == "saarmah002"
    assert data["role"] == "customer"


def test_login_with_wrong_details(client):
    response = client.post(
        "/users",
        json= {
            "name": "Samuel",
            "password": "saarmah"
        }
    )

    response = client.post(
        "/users/login",
        data = {
            "name": "Nana",
            "password": "saarm"
        }
    )
    assert response.status_code == 401
    
    