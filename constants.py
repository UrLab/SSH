import random
import pygame
from pygame.locals import FULLSCREEN

pygame.init()


# BANNER
def CreateBanner(fonts, SCREEN_X):
    title = fonts["50"].render("Simplified Stock Handler", 1, (0, 0, 0))
    urlabImg = pygame.image.load("imgs/UrLabBan.png")
    coef = urlabImg.get_size()[1]/title.get_size()[1]
    urlabImg = pygame.transform.smoothscale(
        urlabImg,
        (
            int(urlabImg.get_size()[0]/coef),
            int(urlabImg.get_size()[1]/coef)
        )
    )

    banner = pygame.Surface((SCREEN_X, 16+urlabImg.get_size()[1]))
    banner.fill((255, 255, 255))
    banner.blit(title, (10, 8))
    banner.blit(urlabImg, (SCREEN_X - 10-urlabImg.get_size()[0], 8))
    pygame.draw.line(
        banner,
        (50, 50, 50),
        (0, 15+urlabImg.get_size()[1]),
        (SCREEN_X, 15+urlabImg.get_size()[1])
    )

    return banner


# FONTS
if random.random() < 0.33:
    fontToLoad = 'fonts/comic-sans-ms.ttf'
else:
    fontToLoad = 'fonts/BebasNeue-Regular.ttf'

fonts = {}
for x in [14, 20, 25, 30, 35, 50, 75, 100]:
    fonts[str(x)] = pygame.font.Font(fontToLoad, x)

SCREEN_X = 1024
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # , FULLSCREEN)

# IMAGES MADE BY THE COMPUTER
urlabBanner = CreateBanner(fonts, SCREEN_X)
background = pygame.image.load("imgs/background.png")
fromUrLabWithLove = fonts["20"].render(
    "Made with love @ UrLab <3", 1, (0, 0, 0))
background.blit(
    fromUrLabWithLove,
    (
        SCREEN_X-fromUrLabWithLove.get_size()[0]-10,
        SCREEN_Y-fromUrLabWithLove.get_size()[1]
    )
)
