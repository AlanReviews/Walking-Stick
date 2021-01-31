import pygame
pygame.init()
background_colour = (135, 206, 235)
screen = pygame.display.set_mode((600,600))
screen.fill(background_colour)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
