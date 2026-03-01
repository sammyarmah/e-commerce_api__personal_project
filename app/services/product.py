from app.schemas.product import ProductCreate, Product
from app.core.product import product_db
from app.utils.file_handler import save_image

class ProductService:

    @staticmethod
    def create_product(product_in: ProductCreate, filename: str):
        product_id = len(product_db) + 1

        
        new_product: Product = Product(
            id= product_id,
            name= product_in.name,
            description= product_in.description,
            price= product_in.price,
            stock= product_in.stock,
            image= filename
        )
        product_db[product_id] = new_product
        return new_product