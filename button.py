import pygame


class Button(object):

    """Represents a button that contains text and handle collisions"""

    def __init__(self, pos, size, text, font):
        self.pos = pos
        self.size = size

        self.fg = (0, 0, 0)
        self.bg = (0, 0, 0)
        self.contour = (50, 50, 50)

        self.font = font
        self.text = text
        self.rect = pygame.Rect(pos, size)
        self.image = font.render(text, 1, self.fg)
        self.text_pos = (
            self.pos[0] + self.size[0]//2 - self.image.get_size()[0]//2,
            self.pos[1] + self.size[1]//2 - self.image.get_size()[1]//2
        )

    def collide(self, pos):
        return self.rect.collidepoint(pos[0], pos[1])

    def set_color(self, fg=None, bg=None, contour=None):
        self.fg = fg if fg is not None else self.fg
        self.bg = bg if bg is not None else self.bg
        self.contour = contour if contour is not None else self.contour

        self.image = self.font.render(self.text, 1, self.fg)

    def draw(self, screen, offset):
        pygame.draw.rect(
            screen, self.contour,
            self.rect.move(offset[0], offset[1]), 2
        )
        screen.blit(
            self.image,
            (self.text_pos[0] + offset[0], self.text_pos[1] + offset[1])
        )
