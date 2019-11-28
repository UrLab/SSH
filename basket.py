from constants import (
    SCREEN_X,
    PRODUCT_X,
    PRODUCT_SMALL_Y
)


class Basket(object):
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def add(self, new_product):
        for index, product in enumerate(self.products):
            if product.name == new_product.name:
                self.products[index].add_one()
                return

        self.add_product(new_product)

    def draw(self, screen):
        for index, product in enumerate(self.products):
            product.draw(
                screen,
                (SCREEN_X//2 - PRODUCT_X//2, 150 + index * PRODUCT_SMALL_Y)
            )
