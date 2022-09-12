import pygame
class Spring(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\toaster-in.png")
        self.image = pygame.transform.scale(self.image, (45, 29))
        self.relaxed = pygame.image.load(r"assets\images\toaster-out.png")
        self.relaxed = pygame.transform.scale(self.image, (40, 53))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates[0], coordinates[1] + 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def update(self, offset):
        self.rect.y += offset

