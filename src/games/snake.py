"""
This is my To do for the start of the snake game

TODO: First generate a white box with pygame
TODO: Generate an object
TODO: Get the object to move with arrows
TODO: Print positions of the object in the terminal
TODO: Make the screen boxed of the object so the object can go passed the size of window
TODO: Snake can only be on the blocks
TODO: Generate an object to eat
TODO: become one block bigger
"""

import pygame

pygame.init()
# Size of the window
HEIGHT = 600
WIDTH = 600
SCREEN = pygame.display.set_mode(size=(HEIGHT, WIDTH))


class Player:
    def __init__(self):
        self.speed = 1
        self.width = 30
        self.height = 30
        self.color = "red"
        self.rect = pygame.Rect(
            (WIDTH - self.width) / 2, (HEIGHT - self.height) / 2, self.width, self.height
        )

    def up(self):
        self.rect.y = max([self.rect.y - self.speed, 0])

    def down(self):
        self.rect.y = min(self.rect.y + self.speed, HEIGHT - self.height)

    def left(self):
        self.rect.x = max([self.rect.x - self.speed, 0])

    def right(self):
        self.rect.x = min(self.rect.x + self.speed, WIDTH - self.width)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)


def drawGrid():
    blocksize = 40

    # Background colors
    color1 = (170, 215, 81)  # Light green
    color2 = (162, 209, 73)  # Darker green

    for x in range(0, WIDTH, blocksize):
        for y in range(0, HEIGHT, blocksize):
            is_even_col = (x // blocksize) % 2 == 0
            is_even_row = (y // blocksize) % 2 == 0
            if (is_even_col and is_even_row) or (not is_even_col and not is_even_row):
                color = color1
            else:
                color = color2
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(SCREEN, color, rect)


char = Player()


while True:
    # Fill the screen with black to clear the previous frame
    SCREEN.fill((0, 0, 0))

    # Quit
    for event in pygame.event.get():  # User does something
        if event.type == pygame.QUIT:
            pygame.quit()

    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        char.up()
    if keys[pygame.K_s]:
        char.down()
    if keys[pygame.K_a]:
        char.left()
    if keys[pygame.K_d]:
        char.right()

    drawGrid()
    char.draw()
    pygame.display.update()
