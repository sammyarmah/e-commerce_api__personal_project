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
   