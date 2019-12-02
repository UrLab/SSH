import pygame
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN


class vkb(object):

    def __init__(self, pos, font):
        self.keys = []
        self.pos = pos
        self.isHidden = True
        self.isShifting = False
        self.size = (500, 235)
        self.rect = pygame.Rect(
            (self.pos[0]-1, self.pos[1]-1),
            (self.size[0]+2, self.size[1]+2)
        )
        self.hidden_rect = pygame.Rect(
            (self.pos[0], self.pos[1] + 195),
            (40, 40)
        )

        self.keys.append(vkey((5,    5), "1", font))
        self.keys.append(vkey((50,   5), "2", font))
        self.keys.append(vkey((95,   5), "3", font))
        self.keys.append(vkey((140,  5), "4", font))
        self.keys.append(vkey((185,  5), "5", font))
        self.keys.append(vkey((230,  5), "6", font))
        self.keys.append(vkey((275,  5), "7", font))
        self.keys.append(vkey((320,  5), "8", font))
        self.keys.append(vkey((365,  5), "9", font))
        self.keys.append(vkey((410,  5), "0", font))
        self.keys.append(vkey((5,    50), "a", font))
        self.keys.append(vkey((50,   50), "z", font))
        self.keys.append(vkey((95,   50), "e", font))
        self.keys.append(vkey((140,  50), "r", font))
        self.keys.append(vkey((185,  50), "t", font))
        self.keys.append(vkey((230,  50), "y", font))
        self.keys.append(vkey((275,  50), "u", font))
        self.keys.append(vkey((320,  50), "i", font))
        self.keys.append(vkey((365,  50), "o", font))
        self.keys.append(vkey((410,  50), "p", font))
        self.keys.append(vkey((455,  50), "<", font))
        self.keys.append(vkey((30,   95), "q", font))
        self.keys.append(vkey((75,   95), "s", font))
        self.keys.append(vkey((120,  95), "d", font))
        self.keys.append(vkey((165,  95), "f", font))
        self.keys.append(vkey((210,  95), "g", font))
        self.keys.append(vkey((255,  95), "h", font))
        self.keys.append(vkey((300,  95), "j", font))
        self.keys.append(vkey((345,  95), "k", font))
        self.keys.append(vkey((390,  95), "l", font))
        self.keys.append(vkey((435,  95), "m", font))
        self.keys.append(vkey((55,  140), "w", font))
        self.keys.append(vkey((100, 140), "x", font))
        self.keys.append(vkey((145, 140), "c", font))
        self.keys.append(vkey((190, 140), "v", font))
        self.keys.append(vkey((235, 140), "b", font))
        self.keys.append(vkey((280, 140), "n", font))
        self.keys.append(vkey((325, 140), "return", font, (120, 40)))
        self.keys.append(vkey((5,   185), "shift", font, (60,  40)))
        self.keys.append(vkey((100, 185), "space", font, (300, 40)))
        self.keys.append(vkey((430, 185), "hide", font, (60,  40)))

        self.textBuffer = ""

    def toggleShow(self):
        self.isHidden = not self.isHidden

    def blit(self, screen):
        if not self.isHidden:
            pygame.draw.rect(screen, (10, 10, 10), self.rect, 1)
            for key in self.keys:
                key.blit(screen, self.pos)
        else:
            pygame.draw.rect(screen, (150, 150, 150), self.hidden_rect, 2)

    def on_event(self, event):
        if not self.isHidden:
            if event.type == MOUSEMOTION:
                for key in self.keys:
                    key.update(
                        (event.pos[0]-self.rect.x, event.pos[1]-self.rect.y))
            if event.type == MOUSEBUTTONDOWN:
                for key in self.keys:
                    if key.collide((event.pos[0]-self.rect.x, event.pos[1]-self.rect.y)):

                        if key.rawVal == "shift":
                            self.isShifting = True
                        elif key.rawVal == "space":
                            self.textBuffer += " "
                        elif key.rawVal == "return":
                            self.textBuffer += "\n"
                        elif key.rawVal == "hide":
                            self.toggleShow()
                        elif key.rawVal == "<":
                            self.textBuffer = self.textBuffer[:-1]
                        else:
                            if self.isShifting:
                                self.textBuffer += key.rawVal.upper()
                                self.isShifting = False
                            else:
                                self.textBuffer += key.rawVal
        else:
            if event.type == MOUSEBUTTONDOWN:
                if self.hidden_rect.collidepoint((event.pos[0], event.pos[1])):
                    self.toggleShow()


class vkey(object):
    def __init__(self, pos, val, font, size=(40, 40)):
        self.font = font
        self.val = self.font.render(val, 1, (20, 20, 20))
        self.rawVal = val
        self.rect = pygame.Rect(pos, size)
        self.isSelected = False

    def collide(self, pos):
        return self.rect.collidepoint(pos)

    def update(self, pos):
        if self.collide(pos):
            self.isSelected = True
        else:
            self.isSelected = False

    def blit(self, screen, pos):
        if not self.isSelected:
            pygame.draw.rect(
                screen, (50, 50, 50), self.rect.move(pos[0], pos[1]), 1)
        else:
            pygame.draw.rect(
                screen, (255, 20, 20), self.rect.move(pos[0], pos[1]), 1)
        screen.blit(
            self.val, (
                self.rect.x + pos[0]
                + self.rect.w/2 - self.val.get_size()[0]/2,
                self.rect.y + pos[1]
                + self.rect.h/2 - self.val.get_size()[1]/2
            )
        )
