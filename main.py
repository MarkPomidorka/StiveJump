import pygame
import sys
import random
from sprites.platforms import Platform
from sprites.steve import Steve
pygame.init()

# Константы/Constants
WIDTH = 800
HEIGHT = 600
FPS = 60


# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Steve Jump")


clock = pygame.time.Clock()



def main():
    offset = 0
    # Спрайты/Sprites
    platforms = pygame.sprite.Group()
    player = Steve()
    for y in range(25,screen.get_height(),50):
        x = random.randint(100,screen.get_width()-100)
        platforms.add(Platform((x,y)))

    quantity = len(platforms)

    offset = 0

    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if player.rect.bottom < screen.get_height() / 2:
            offset = 10
        else:
            offset = 0

        for platform in platforms:
            if (platform.rect.collidepoint(player.rect.bottomleft) or \
                platform.rect.collidepoint(player.rect.bottomright)) and player.gravity <= 0:
                player.gravity = 15

                #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #main()



        # Рендеринг/Rendering

        screen.fill((255, 138, 5))
        for x in range(0, screen.get_width(), 20):
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), 20):
            pygame.draw.line(screen, (0, 0, 0), (0, y), (screen.get_width(),y))
            quantity = len(platforms)

        platforms.draw(screen)
        player.draw(screen)



        # Обновление спрайтов/Updating sprites

        platforms.update(offset)
        player.update(offset)
        if quantity > len(platforms):
            x = random.randint(100, screen.get_width() - 100)
            platform = Platform((x, 0))
            platforms.add(platform)

        # Обновление экрана/Screen Refresh




        pygame.display.update()

if __name__ == "__main__":
    main()
