from fastapi.testclient import TestClient
from app.core.user import user_db
from app.main import app
from app.dependency import is_admin_user, is_customer_user
import pytest


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clear_user_db():
    user_db.clear()

@pytest.fixture
def is_admin():
    fake_admin_user = {
        "id": 1,
        "role": "admin"
    }

    def admin_override(user_id: int = 1):
        return fake_admin_user["id"]
    
    app.dependency_overrides[is_admin_user] = admin_override
    yield fake_admin_user
    app.dependency_overrides = {}
    


    