from fastapi import APIRouter, status, Depends, File, UploadFile, Form
from app.schemas.product import ProductCreate
from app.services.product import ProductService
from app.dependency import is_admin_user


product_router = APIRouter()

@product_router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    image: UploadFile = File(...),
    current_user: int = Depends(is_admin_user)
    
):
    product_in = ProductCreate(
        name = name,
        description = description,
        price = price,
        stock = stock
    )
    return ProductService.create_product(product_in, image.filename)
