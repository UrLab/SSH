import pygame
from constants import (
    PRODUCT_X,
    PRODUCT_Y,
    PRODUCT_SMALL_Y,
    fonts
)


class Product(object):
    def __init__(self, name, price, image="imgs/products/Not_Found.png", nb=1):
        self.name = name
        self.price = price
        image = pygame.image.load(image)
        self.nbr = nb

        # Coefficient for resizing the image at the desired size
        coef_full = image.get_size()[1]/(PRODUCT_Y - 6)
        coef_small = image.get_size()[1]/(PRODUCT_SMALL_Y - 6)

        self.text_img = fonts["25"].render(
            "{}x {}".format(self.nbr, self.name),
            1, (0, 0, 0)
        )

        self.full_image = pygame.transform.smoothscale(
            image,
            (
                int(image.get_size()[0]/coef_full),
                int(image.get_size()[1]/coef_full)
            )
        )
        self.small_image = pygame.transform.smoothscale(
            image,
            (
                int(image.get_size()[0]/coef_small),
                int(image.get_size()[1]/coef_small)
            )
        )

    def add_one(self):
        self.nbr += 1
        self.text_img = fonts["25"].render(
            "{}x {}".format(self.nbr, self.name),
            1, (0, 0, 0)
        )

    def draw(self, screen, pos, last=False):
        if last:
            rect = pygame.Rect(pos, (PRODUCT_X, PRODUCT_Y))

            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            screen.blit(
                self.full_image, (
                    pos[0] + PRODUCT_X - self.full_image.get_size()[0],
                    pos[1] + 3,
                )
            )
        else:
            rect = pygame.Rect(pos, (PRODUCT_X, PRODUCT_SMALL_Y))

            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            screen.blit(
                self.text_img, (
                    pos[0] + 5,
                    pos[1] + PRODUCT_SMALL_Y//2 - self.text_img.get_size()[1]//2
                )
            )

            screen.blit(
                self.small_image, (
                    pos[0] + PRODUCT_X - self.small_image.get_size()[0] - 5,
                    pos[1] + 3,
                )
            )
