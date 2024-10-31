from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.product_model import Product

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_product(self, product_name: str, price: float, product_description: str = None):
        product = Product(product_name = product_name,  price = price, product_description = product_description,)
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def get_products(self):
        query = select(Product)
        result = await self.db.execute(query)
        return result.scalars().all()  

    async def get_product_by_id(self, product_id: int):
        query = select(Product).where(Product.product_id == product_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()