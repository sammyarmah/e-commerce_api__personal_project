from fastapi import APIRouter, status, Depends, File, UploadFile, Form
from app.schemas.product import ProductCreate, ProductUpdate
from app.services.product import ProductService
from app.dependency import is_admin_user
from typing import Optional


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
    # Extract data from file uploaded
    file_bytes = image.file.read()
    filename = image.filename
    
    return ProductService.create_product(product_in, file_bytes, filename)

@product_router.get("/")
def get_all_products(name: Optional[str] = None):
    return ProductService.get_all_products(name)

@product_router.get("/{id}")
def get_product_by_id(id: int):
    return ProductService.get_product_by_id(id)

@product_router.put("/{id}")
def update_product(id: int, product_data: ProductUpdate ,current_user: int = Depends(is_admin_user)):
    return ProductService.update_product(id, product_data)

@product_router.delete("/{id}")
def delete_product(id: int, current_user: int = Depends(is_admin_user)):
    ProductService.delete_product(id)
    return {"message": "Product deleted successfully"}