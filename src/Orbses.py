#Orbses
import pygame,sys
pygame.init()

# ======= Constants =======

# Pygame Window constants / setup
WIDTH, HEIGHT = 852, 480

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
#BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
#BACKGROUND_RECT = BACKGROUND.get_rect(center=(317,300))
ICON = pygame.image.load("assets/orbses1.png")

pygame.display.set_caption("Orbses")
pygame.display.set_icon(ICON)

# Screen Init
SCREEN.fill((127,127,127))
pygame.display.flip()
#SCREEN.blit(BACKGROUND, BACKGROUND_RECT)

while True: # main game loop

    for event in pygame.event.get():
        SCREEN.fill((127,127,127))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()