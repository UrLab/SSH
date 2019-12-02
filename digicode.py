from button import Button


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
