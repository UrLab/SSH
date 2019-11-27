import pygame
from database import DataBase
from pygame.locals import (
    QUIT,
    K_RETURN,
    K_BACKSPACE,
    KEYDOWN,
    K_ESCAPE
)

from constants import (
    fonts,
    screen,
    urlabBanner,
    background,
    SCREEN_X,
    SCREEN_Y
)


# Get the scan result
def fetchScan(event, text):
    if event.type == KEYDOWN:
        if event.key == K_RETURN:
            return text, True
        elif event.key == K_BACKSPACE:
            text = text[:-1]
        else:
            text += str((event.scancode-9) % 10)
    return text, False


def main():
    db = DataBase('data/db.json')
    scan = "", False
    running = True
    title = fonts["25"].render(
        "Scannez un produit pour en connaitre sa valeur", 1, (0, 0, 0))
    current_product = [None, None, None]

    while running:
        screen.blit(background, (0, 0))
        screen.blit(urlabBanner, (0, 0))
        screen.blit(title, (10, urlabBanner.get_size()[1]+10))
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (15, urlabBanner.get_size()[1]+title.get_size()[1]+10),
            (0.9*SCREEN_X, urlabBanner.get_size()[1]+title.get_size()[1]+10)
        )

        if current_product[2] is not None:
            screen.blit(
                current_product[2], (
                    SCREEN_X//2 - current_product[2].get_size()[0]//2,
                    SCREEN_Y//2 - current_product[2].get_size()[1]//2
                    + 30
                )
            )
            screen.blit(
                current_product[0], (
                    SCREEN_X//2 - current_product[0].get_size()[0]//2,
                    SCREEN_Y//2 - current_product[2].get_size()[1]//2
                    - current_product[0].get_size()[1]
                    + 30
                )
            )
            screen.blit(
                current_product[1], (
                    SCREEN_X//2 - current_product[1].get_size()[0]//2,
                    SCREEN_Y//2 + current_product[2].get_size()[1]//2
                    + 30,
                )
            )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            scan = fetchScan(event, scan[0])
            if scan[1]:
                current_product = db.fetch(scan[0])
                if current_product[0] == "":
                    current_product[0] = "Not found !"
                    current_product[1] = "99999999999"
                if current_product[2] == "":
                    current_product[2] = "imgs/products/Not_Found.png"
                current_product = [
                    fonts["25"].render(
                        current_product[0],
                        1,
                        (0, 0, 0)
                    ),
                    fonts["50"].render(
                        "{}€".format(current_product[1]),
                        1,
                        (0, 0, 0)
                    ),
                    pygame.image.load(current_product[2])
                ]
                # Coefficient for resizing the image at the desired size
                coef = current_product[2].get_size()[1]/150

                current_product[2] = pygame.transform.smoothscale(
                    current_product[2],
                    (
                        int(current_product[2].get_size()[0]/coef),
                        int(current_product[2].get_size()[1]/coef)
                    )
                )

                scan = "", False

        pygame.display.flip()


if __name__ == "__main__":
    main()
