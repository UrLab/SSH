from constants import (
    msg_colors,
    fonts,
    SCREEN_Y
)


class Message(object):
    """ Displays a message on the screen for a certain amout of time """

    def __init__(self, text, type, time=3):
        self.image = fonts["20"].render(text, 1, msg_colors[type])
        self.time = time

    def draw(self, screen, offset):
        if SCREEN_Y - 100 - (30*offset) > 120:
            screen.blit(self.image, (15, SCREEN_Y - 100 - (30*offset)))

    def update(self, time_elapsed):
        self.time -= time_elapsed
        return self.time <= 0
