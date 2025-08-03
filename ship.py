import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.image=pygame.transform.rotate(self.image,270)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        self.y=float(self.rect.y)
        self.moving_down=False
        self.moving_up= False
    def update(self):
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y +=self.settings.ship_speed
        if self.moving_up and self.rect.top >0 :
            self.y -=self.settings.ship_speed
        self.rect.y=self.y
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)