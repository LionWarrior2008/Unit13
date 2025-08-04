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
        score_str=f'Score






        pass