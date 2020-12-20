import pygame


class Ship:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def changeDirection(self, moving_right, moving_left, moving_up, moving_down):
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.moving_up = moving_up
        self.moving_down = moving_down

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and 0 < self.rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
        self.cycleCoordinates()

    def cycleCoordinates(self):
        self.rect.x = self.rect.x%self.screen_rect.width
        self.rect.y = self.rect.y%self.screen_rect.height

    def checkLocation(self):
        return 0 < self.rect.left and self.rect.right < self.screen_rect.right and 0 < self.rect.bottom and self.rect.top < self.screen_rect.top

    def drawme(self):
        self.screen.blit(self.image, self.rect)