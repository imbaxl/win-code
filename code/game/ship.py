import pygame

class ship():
    def __init__(self,screen):
       self.screen = screen

       #加载飞船图像和外接矩形
       self.image = pygame.image.load('code/game/image/plane.png')
       self.rect = self.image.get_rect()
       self.screen_rect = screen.get_rect()


       #每艘新飞船放在屏幕底部中间
       self.rect.centerx = self.screen_rect.centerx
       self.rect.bottom = self.screen_rect.bottom

       #移动标志
       self.moving_right = False
       self.moving_left = False
       self.moving_up = False
       self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        elif self.moving_up:
            self.rect.bottom -= 1
        elif self.moving_down:
            self.rect.bottom += 1


    def blitme(self):
        #绘制飞船
        self.screen.blit(self.image, self.rect)