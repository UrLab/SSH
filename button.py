import pygame


class Button(object):

    """Represents a button that contains text and handle collisions"""

    def __init__(self, pos, size, text, font):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos, size)
        self.image = font.render(text, 1, (0, 0, 0))
        self.text_pos = (
            self.pos[0] + self.size[0]//2 - self.image.get_size()[0]//2,
            self.pos[1] + self.size[1]//2 - self.image.get_size()[1]//2
        )

    def collide(self, pos):
        return self.rect.collidepoint(pos[0], pos[1])

    def draw(self, screen, offset):
        pygame.draw.rect(
            screen, (50, 50, 50),
            self.rect.move(offset[0], offset[1]), 2
        )
        screen.blit(
            self.image,
            (self.text_pos[0] + offset[0], self.text_pos[1] + offset[1])
        )
