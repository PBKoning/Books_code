# pygame demo 4(b) - one image, bounce around the window using rects and making sounds

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
IMAGES_PATH = "./Object-Oriented Python - Master OOP by Building Games and GUIs/Chapter 5/02 Drawing an image/images/"
SOUNDS_PATH = "./Object-Oriented Python - Master OOP by Building Games and GUIs/Chapter 5/02 Drawing an image/sounds/"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load(IMAGES_PATH+'ball.png')
bounceSound = pygame.mixer.Sound(SOUNDS_PATH+'boing.wav')
pygame.mixer.music.load(SOUNDS_PATH+'background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed # reverse X direction
        bounceSound.play()
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed # reverse Y direction
        bounceSound.play()

    # Update the ball's rectangle using the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    
    # 9 - Clear the window before drawing it again 
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    window.blit(ballImage, ballRect)
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)