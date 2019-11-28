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


class DigiCode(object):

    """ Represents a 10 buttons digicode """

    def __init__(self, pos, font, case_size=30, gap_size=5):
        self.buttons = []
        self.pos = pos
        for y in range(3):
            for x in range(3):
                self.buttons.append(
                    Button(
                        (x*(case_size+gap_size), y*(case_size+gap_size)),
                        (case_size, case_size), str(y*3+x+1), font
                    )
                )

        self.buttons.append(
            Button(
                (0, 3*(case_size+gap_size)),
                (case_size, case_size), "X", font
            )
        )
        self.buttons.append(
            Button(
                ((case_size+gap_size), 3*(case_size+gap_size)),
                (case_size, case_size), "0", font
            )
        )
        self.buttons.append(
            Button(
                (2*(case_size+gap_size), 3*(case_size+gap_size)),
                (case_size, case_size), "OK", font
            )
        )

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen, self.pos)
