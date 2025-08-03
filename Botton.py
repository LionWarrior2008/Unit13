import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Botton:
    def __init__(self,game:'AlienInvasion',msg):
        self.game=game
        self.screen=game.screen
        self.bounderies=game.screen.get_rect()
        self.settings=game.settings
        self.font=pygame.font.Font(self.settings.font_style,self.settings.botton_font_size)
        self.rect=pygame.Rect(0,0,self.settings.botton_w,self.settings.botton_h)
        self.rect.center=self.bounderies.center
        self.__prep__msg(msg)
    def __prep__msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.settings.text_color,None)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw(self):
        self.screen.fill(self.settings.botton_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
    def check_clicked(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)