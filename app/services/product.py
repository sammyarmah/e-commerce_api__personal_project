from fastapi import HTTPException, status
from app.schemas.product import ProductCreate, Product, ProductUpdate
from app.core.product import product_db
from app.utils.file_handler import save_file
from typing import Optional

class ProductService:

    @staticmethod
    def create_product(product_in: ProductCreate, file_bytes: bytes, filename: str):
        saved_filename = save_file(file_bytes, filename)

        product_id = len(product_db) + 1

        
        new_product: Product = Product(
            id= product_id,
            name= product_in.name,
            description= product_in.description,
            price= product_in.price,
            stock= product_in.stock,
            image= saved_filename
        )
        product_db[product_id] = new_product
        return new_product
    
    @staticmethod
    def get_all_products(name: Optional[str] = None):
        if not name:
            return list(product_db.values())
        
        product_list = []

        if name:
            for product in product_db.values():
                if product.name == name:
                    product_list.append(product)
        return product_list
    
    @staticmethod
    def get_product_by_id(id: int):
        product = product_db.get(id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Product not found"
            )
        return product
    
    @staticmethod
    def update_product(id:int, product_data: ProductUpdate):
        product = product_db.get(id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Product not found"
            )
        
        update_product = product_data.model_dump(exclude_unset = True)

        for key, value in update_product.items():
            setattr(product, key, value)

        return product


    @staticmethod
    def delete_product(product_id: int):
        product = product_db.get(product_id)
        if not product:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "Product not found"
            )
        
        del product_db[product_id ]