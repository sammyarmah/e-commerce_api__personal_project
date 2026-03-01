from fastapi import FastAPI
from app.api.v1.user import user_router
from app.api.v1.product import product_router


app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/products", tags=["Products"])