from typing import List, Optional

from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, name: str) -> Optional[Product]:  # None or Product
        res = [p for p in self.products if p.name == name]
        if res:
            return res[0]

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
