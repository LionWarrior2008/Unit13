import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class Hud:
    def __init__(self,game:'AlienInvasion'):
        self.game=game
        self.settings=game.settings
        self.screen=game.screen
        self.bounderes=self.game.screen.get_rect()
        self.game_stats=game.game_stats
        self.font=pygame.font.Font(self.settings.font_style,self.settings.hud_font_size)
        self.padding=20
        self.update_scores()
        self.setup_life_image()
        self.update_level()
    def update_scores(self):
        self._update_score()
        self._update_high_score()
        self._update_max_score()
    def _update_score(self):
        score_str=f'Score:{self.game_stats.score: ,.0f}'
        self.score_image=self.font.render(score_str,True,self.settings.text_color,None)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.bounderes-self.padding
        self.score_rect.top=self.max_score_rect.bottom+self.padding
    def _update_max_score(self):
        max_score_str=f'Max-Score:{self.game_stats.max_score: ,.0f}'
        self.max_score_image=self.font.render(max_score_str,True,self.settings.text_color,None)
        self.max_score_rect=self.max_score_image.get_rect()
        self.max_score_rect.right=self.bounderes-self.padding
        self.max_score_rect.top=self.padding
    def _update_max_score(self):
        High_score_str=f'High-Score:{self.game_stats.high_score: ,.0f}'
        self.High_score_image=self.font.render(High_score_str,True,self.settings.text_color,None)
        self.High_score_rect=self.High_score_image.get_rect()
        self.High_score_rect.midtop=(self.bounderes.centerx,self.padding)
    def draw(self):
        self.screen.blit(self.High_score_image,self.High_score_rect)
        self.screen.blit(self.max_score_image,self.max_score_rect)
        self.screen.blit(self.score_image,self.score_rect)





        pass