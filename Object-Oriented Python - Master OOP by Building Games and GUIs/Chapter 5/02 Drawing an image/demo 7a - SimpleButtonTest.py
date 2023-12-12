# Pygame demo 7 - SimpleButton test

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from SimpleButton import * # bring in the SimpleButton class code

# 2 - Define constants
GRAY = (128, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
IMAGES_PATH = "./Object-Oriented Python - Master OOP by Building Games and GUIs/Chapter 5/02 Drawing an image/images/"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
# Create an instance of a SimpleButton
oButton = SimpleButton(window, (150, 30), IMAGES_PATH+'buttonUp.png', IMAGES_PATH+'buttonDown.png')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if it has been clicked on
        if oButton.handleEvent(event):
            print('User has clicked the button')
        
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
        window.fill(GRAY)

    # 10 - Draw all window elements
    oButton.draw() # draw the button

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)