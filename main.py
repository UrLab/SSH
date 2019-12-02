import pygame
import time

from pygame.locals import (
    QUIT,
    K_RETURN,
    K_BACKSPACE,
    KEYDOWN,
    K_ESCAPE,
    MOUSEBUTTONDOWN
)

from constants import (
    fonts,
    screen,
    urlabBanner,
    background,
    SCREEN_X,
    SCREEN_Y
)
from database import DataBase
from digicode import DigiCode
from product import Product
from cart import Cart
from button import Button
from message import Message


# Get the cleaned scan result
def fetchScan(event, text):
    if event.type == KEYDOWN:  # Get every input from the scan
        # The "return" key is the final input from the scan
        if event.key == K_RETURN:
            return text, True
        elif event.key == K_BACKSPACE:
            text = text[:-1]
        else:
            # event.scancode automatically converts the result as string
            text += str((event.scancode-9) % 10)
    return text, False


def pay(cart, messages):
    if cart.is_empty():
        messages.insert(0, Message("Votre panier est vide !", "ERROR"))
        return

    print("proceeding")


def main():
    # Handles the data from a json file, needs to be upgraded
    db = DataBase('data/db.json')

    # The result is a string containing the scan value and a
    # boolean indicating if its the complete scan or not
    scan = "", False
    cart = Cart()
    buttons = {
        "cancel": Button(
            (10, 540), (275, 50), "Annuler tous les achats", fonts["25"]),
        "proceed": Button(
            (SCREEN_X//2 - 275//2, 540), (275, 50), "Payer", fonts["25"]),
    }

    buttons["cancel"].set_color(fg=(200, 10, 10))
    buttons["proceed"].set_color(fg=(10, 200, 10))

    running = True  # Defines wether the application is running or not
    finnish = False  # Defines wether the user wants to pay or not

    title = fonts["25"].render(
        "Scannez un produit pour en connaitre sa valeur", 1, (0, 0, 0))
    # The current product (Name, Price, Image) as images
    current_product = [None, None, None]

    # The digicode widget
    digicode = DigiCode(
        (SCREEN_X - 250, SCREEN_Y//2 - 80),
        fonts["25"], case_size=60, gap_size=5
    )

    start_time = time.time()
    messages = []

    while running:
        time_elapsed = time.time() - start_time
        start_time = time.time()

        screen.blit(background, (0, 0))
        screen.blit(urlabBanner, (0, 0))
        screen.blit(title, (10, urlabBanner.get_size()[1]+10))
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (15, urlabBanner.get_size()[1]+title.get_size()[1]+10),
            (0.9*SCREEN_X, urlabBanner.get_size()[1]+title.get_size()[1]+10)
        )

        if finnish:
            digicode.draw(screen)

        cart.draw(screen)

        for button in buttons.values():
            button.draw(screen, (0, 0))

        for x, message in enumerate(messages):
            message.draw(screen, x)
            if message.update(time_elapsed):
                del messages[messages.index(message)]

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Fetching Quit key
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            # Fetch click ( = touch) events
            elif event.type == MOUSEBUTTONDOWN:
                if buttons["proceed"].collide(event.pos):
                    pay(cart, messages)
                elif buttons["cancel"].collide(event.pos):
                    cart.empty()

            scan = fetchScan(event, scan[0])
            # If a scan has been completed
            if scan[1]:
                current_product = db.fetch(scan[0])
                # If no product was found with the scan
                if current_product[0] != "":
                    messages.insert(
                        0,
                        Message(
                            "Ajouté : {}".format(current_product[0]),
                            "SUCCESS"
                        )
                    )

                    # If there's no image associated to the product
                    if current_product[2] == "":
                        messages.insert(0, Message("Pas d'image", "WARNING"))
                        current_product[2] = "imgs/products/Not_Found.png"

                    current_product = Product(
                        current_product[0],
                        current_product[1],
                        current_product[2]
                    )

                    cart.add(current_product)
                else:
                    messages.insert(
                        0, Message("Aucun produit trouvé !", "ERROR"))

                scan = "", False

        pygame.display.flip()


if __name__ == "__main__":
    main()
