import pygame
class Platform(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        if random.randint(1,100) in range (1,11):
            if random.randint(1, 100) in range(1, 11):
             self.image = pygame.image.load(r"assets\images\.png")
             self.color = "blue"
        self.rect.center = coordinates
        self.image = pygame.transform.scale(self.image, (180, 70))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, offset):
        self.rect.y += offset
        surface = pygame.display.get_surface()
        if self.rect.top > surface.get_height():
            self.kill()

            #Hello World!#
