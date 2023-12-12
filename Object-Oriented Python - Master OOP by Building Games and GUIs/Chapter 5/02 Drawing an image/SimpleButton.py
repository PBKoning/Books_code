# SimpleButton class
#
# Uses a "state machine" approach
#

import pygame
from pygame.locals import *


class SimpleButton():

    # Used to track the state of the button
    STATE_IDLE = 'idle' # button is up, mouse not over button
    STATE_ARMED = 'armed' # button is down, mouse over button
    STATE_DISARMED = 'disarmed' # clicked down on button, rolled off

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
    
        # Get the rect of the button (used to see if the mouse is over the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]
        self.state = SimpleButton.STATE_IDLE
    
    def handleEvent(self, eventObj):
        # This method will return True if user clicks the button.
        # Normally returns False.
      
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:                               # Als state==Idle...
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:   # en er wordt geklikt op de knop...
                self.state = SimpleButton.STATE_ARMED                           # wordt de state Armed                
            
        elif self.state == SimpleButton.STATE_ARMED:                            # Als de state==Armed...
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:     # en de muis is losgelaten op de knop...
                self.state = SimpleButton.STATE_IDLE                            # wordt de state weer Idle...
                return True # clicked!                                          # en wordt geretourneerd dat er is geklikt
            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect): # Als de muis wordt bewogen en niet meer op knop zit...
                self.state = SimpleButton.STATE_DISARMED                        # wordt de state Disarmed 
            
        elif self.state == SimpleButton.STATE_DISARMED:                         # Als de state==Disarmed...
            if eventPointInButtonRect:                                          # en de muis weer op de knop is...
                self.state = SimpleButton.STATE_ARMED                           # wordt de state Armed
            elif eventObj.type == MOUSEBUTTONUP:                                # maar als de muis omhoog gaat en dus niet op de knop is...
                self.state = SimpleButton.STATE_IDLE                            # wordt de state Idle

        return False                                                            # Retourneer False voor alles wanneer er niet geklikt is    

    def draw(self):
        # Draw the button's current appearance to the window
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        else: # IDLE or DISARMED
            self.window.blit(self.surfaceUp, self.loc)