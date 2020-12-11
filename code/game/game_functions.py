import sys
import pygame 

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 20
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -= 20
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.rect.bottom -= 20
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.rect.bottom += 20
                ship.moving_down = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


        

def update(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
    

