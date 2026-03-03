def test_create_product(client, is_admin):
    create_response = client.post(
        "/products/",
        data= {
            "name": "Laptop",
            "description": "HP Laptop Core i5, 32 GIG RAM",
            "price": 2500.80,
            "stock": 3
        },
        files={
            "image": ("test.jpg", b"fake image", "image/jpeg")
        }
    )
    assert create_response.status_code == 201
    assert create_response.json()["name"] == "Laptop"

def test_create_product_by_customer(client, is_customer):
    response = client.post(
        "/products/",
        data = {
            "name": "Laptop",
            "description": "Good Laptop",
            "price": 2500,
            "stock": 4
        },
        files= {
            "image": ("test.jpg", b"fake image", "image/jpeg")
        }
    )
    assert response.status_code == 403

def test_create_product_with_missing_fields(client, is_admin):
    response = client.post(
        "/products/",
        data = {
            "name": "Laptop",
            "description": "Good Laptop",
            "stock": 3
        }
    )
    assert response.status_code == 422

def test_get_all_products(client, is_admin):
    response = client.post(
        "/products/",
        data = {
            "name": "Phone",
            "description": "Samsung",
            "price": 2500.0,
            "stock": 10
        },
        files = {
            "image": ("test.jpg", b"fake image", "image/jpeg")
        }
    )
    assert response.status_code == 201

    get_response = client.get("/products/")
    assert get_response.status_code == 200
    
def test_get_product_by_id(client, is_admin):
    response = client.post(
        "/products/",
        data = {
            "name": "Phone",
            "description": "Iphone",
            "price": 4500.30,
            "stock": 8
        },
        files = {
            "image": ("test.jpg", b"fake image", "image/jpeg")
        }
    )
    assert response.status_code == 201

    product_id = response.json()["id"]
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 200

def test_update_product(client, is_admin):
    response = client.post(
        "/products/",
        data = {
            "name": "Shoes",
            "description": "Size 45 and 48 available",
            "price": 250.30,
            "stock": 4
        },
        files= {
            "image": ("test.jpg", b"fake image", "image/jpeg")
        }
    )
    assert response.json()["price"] == 250.30

    product_id = response.json()["id"]

    update_response = client.put(
        f"/products/{product_id}",
        json = {
            "price": 300.23,
            "stock": 9
        }
    )
    assert update_response.status_code == 200
    assert update_response.json()["price"] == 300.23


def test_delete_product(client, is_admin):
    create_response = client.post(
        "/products/",
        data = {
            "name": "Curtains",
            "description": "we have white and pink available",
            "price": 300.2,
            "stock": 8
        },
        files = {
            "image": ("test.jpg", b"fake image", "image/jpg")
        }
    )
    
    product_id = create_response.json()["id"]
    
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.json()["message"] == "Product deleted successfully"

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404

    
   