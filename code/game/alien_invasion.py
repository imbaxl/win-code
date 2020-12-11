import pygame
from settings import settings
from ship import ship
import game_functions as gf

def run_game():
    #初始化
    pygame.init()
    ai_settings = settings()
    #创建屏幕对象
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship_new = ship(screen)


    #开始主循环
    while True:
        gf.check_events(ship_new)
        gf.update(ai_settings, screen, ship_new)
        ship_new.update()



run_game_new = run_game()