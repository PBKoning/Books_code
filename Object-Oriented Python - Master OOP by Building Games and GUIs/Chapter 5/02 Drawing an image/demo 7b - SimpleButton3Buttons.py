# Pygame demo 7 - SimpleButton 3 buttons

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
oButtonA = SimpleButton(window, (25, 30), IMAGES_PATH+'buttonAUp.png', IMAGES_PATH+'buttonADown.png')
oButtonB = SimpleButton(window, (150, 30), IMAGES_PATH+'buttonBUp.png', IMAGES_PATH+'buttonBDown.png')
oButtonC = SimpleButton(window, (275, 30), IMAGES_PATH+'buttonCUp.png', IMAGES_PATH+'buttonCDown.png')


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to each button, see if one has been clicked
        if oButtonA.handleEvent(event):
             print('User clicked button A.')
        elif oButtonB.handleEvent(event):
             print('User clicked button B.')
        elif oButtonC.handleEvent(event):
            print('User clicked button C.')
        
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
        window.fill(GRAY)

    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)