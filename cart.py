from constants import (
    SCREEN_X,
    SCREEN_Y,
    PRODUCT_X,
    PRODUCT_SMALL_Y,
    fonts
)


class Cart(object):
    def __init__(self):
        self.products = []
        self.total = 0
        self.total_price = fonts["30"].render(
            "Total : {}€".format(self.total),
            1, (0, 0, 0)
        )

    def add_product(self, product):
        self.products.append(product)

    def recompute_total(self):
        self.total = 0
        for product in self.products:
            self.total += product.get_total()
        self.total_price = fonts["30"].render(
            "Total : {}€".format(self.total),
            1, (0, 0, 0)
        )

    def add(self, new_product):
        for index, product in enumerate(self.products):
            if product.name == new_product.name:
                self.products[index].add_one()
                self.recompute_total()
                return

        self.add_product(new_product)
        self.recompute_total()

    def is_empty(self):
        return len(self.products) == 0

    def empty(self):
        self.products = []
        self.recompute_total()

    def draw(self, screen):
        for index, product in enumerate(self.products):
            if index == len(self.products) - 1:
                product.draw(
                    screen,
                    (SCREEN_X//2 - PRODUCT_X//2, 150 + index*PRODUCT_SMALL_Y),
                    last=True
                )
            else:
                product.draw(
                    screen,
                    (SCREEN_X//2 - PRODUCT_X//2, 150 + index * PRODUCT_SMALL_Y)
                )
        screen.blit(
            self.total_price, (
                SCREEN_X//2 - self.total_price.get_size()[0]//2,
                SCREEN_Y - 110
            )
        )
