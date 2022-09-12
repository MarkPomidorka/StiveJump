import pygame
import random
class Platform(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        if random.randint(1,100) in range (1,11):
            self.image = pygame.image.load(r"assets\images\Pan.png")
            self.color = "blue"
        elif random.randint(1, 100) in range(1, 11):
            self.image = pygame.image.load(r"assets\images\stove-off.png")
            self.image = pygame.transform.scale(self.image,(116,58))
            self.broken = pygame.image.load(r"assets\images\stove-0n.png")
            self.broken = pygame.transform.scale(self.broken,(116,116))

            self.color = "red"
        else:
            self.image = pygame.image.load(r"assets\images\pancakes.png")
            self.image = pygame.transform.scale(self.image,(116,58))
            self.color = "green"

        self.rect = self.image.get_rect()
        self.rect.midbottom = coordinates
        self.step = 5
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, offset):
        self.rect.y += offset
        surface = pygame.display.get_surface()
        if self.rect.top > surface.get_height():
            self.kill()

        if self.color == 'blue':
            self.rect.x += self.step
            if self.rect.centerx > surface.get_width()-50 or self.rect.centerx < -50:
                self.step *= -1