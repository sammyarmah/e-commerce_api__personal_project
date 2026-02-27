def test_register_user(client):
    response = client.post(
        "/users/",
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

def test_login_with_wrong_credentials(client):
    create_response = client.post(
        "/users/",
        json = {
            "name": "Samuel",
            "email": "saarmah@gmail.com",
            "password": "saarmah0002rg",
            "role": "customer"
        }
    )
    assert create_response.status_code == 201
    
    response = client.post(
        "/users/login",
        data= {
            "name": "Samuel",
            "password": "saarmah"
        }
    )
    assert response.status_code == 401

def test_login_password_too_short(client):
    response = client.post(
        "/users/login",
        data = {
            "name": "Nana",
            "password": "saarm"
        }
    )
    assert response.status_code == 401

def test_login_success(client):
    create_response = client.post(
        "/users/",
        json = {
            "name": "Samuel",
            "email": "saarmah@gmail.com",
            "password": "saarmah0002rg",
            "role": "customer"
        }
    )
    assert create_response.status_code == 201

    response = client.post(
        "/users/login",
        data = {
            "name": "Samuel",
            "password": "saarmah0002rg"
        }
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_get_all_users(client, is_admin):
    create_response = client.post(
        "/users/",
        json = {
            "name": "Samuel",
            "email": "samuelarmah@gmail.com",
            "password": "saarmah002",
            "role": "admin"
        }
    )
    assert create_response.status_code == 201

    # Get all users
    response = client.get("/users/")
    assert response.status_code == 200 

def test_admin_get_all_users_by_id(client, is_admin):
    response = client.post(
        "/users/",
        json = {
            "name": "Samuel",
            "email": "samuelarmah@gmail.com",
            "password": "saarmah002",
            "role": "admin"
        }
    )
    assert response.status_code == 201
    user_id = response.json()["id"]
                                  
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["name"] == "Samuel"
    