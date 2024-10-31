from sqlalchemy.ext.asyncio import AsyncSession
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: AsyncSession):
        self.repository = ProductRepository(db)

    async def create_product(self, product_name: str, price: float ,product_description: str = None):
        return await self.repository.create_product(product_name, price, product_description)

    async def get_product_by_id(self, product_id: int):
        return await self.repository.get_product_by_id(product_id)

    async def get_products(self):
        return await self.repository.get_products()