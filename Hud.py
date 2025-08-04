import pygame.font

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
        self._update_level()
    def setup_life_image(self):
        self.life_image=pygame.image.load(self.settings.ship_file)
        self.life_image=pygame.transform.scale(self.life_image,(self.settings.ship_w,self.settings.ship_h))
        self.life_rect=self.life_image.get_rect()
    def update_scores(self):
        self._update_max_score()
        self._update_High_score()
        self._update_score()
    def _update_score(self):
        score_str=f'Score:{self.game_stats.score: ,.0f}'
        self.score_image=self.font.render(score_str,True,self.settings.text_color,None)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.bounderes.right-self.padding
        self.score_rect.top=self.max_score_rect.bottom+self.padding
    def _update_max_score(self):
        max_score_str=f'Max-Score:{self.game_stats.max_score: ,.0f}'
        self.max_score_image=self.font.render(max_score_str,True,self.settings.text_color,None)
        self.max_score_rect=self.max_score_image.get_rect()
        self.max_score_rect.right=self.bounderes.right-self.padding
        self.max_score_rect.top=self.padding
    def _update_High_score(self):
        High_score_str=f'High-Score:{self.game_stats.high_score: ,.0f}'
        self.High_score_image=self.font.render(High_score_str,True,self.settings.text_color,None)
        self.High_score_rect=self.High_score_image.get_rect()
        self.High_score_rect.midtop=(self.bounderes.centerx,self.padding)
    def _update_level(self):
        level_str=f'Level:{self.game_stats.level: ,.0f}'
        self.level_image=self.font.render(level_str,True,self.settings.text_color,None)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.left=self.padding
        self.level_rect.top=self.life_rect.bottom+self.padding
    def draw_lifes(self):
        current_x=self.padding
        current_y=self.padding
        for i in range(self.game_stats.ship_left):
            self.screen.blit(self.life_image,(current_x,current_y))
            current_x+=self.life_rect.width+self.padding
    def draw(self):
        self.screen.blit(self.High_score_image,self.High_score_rect)
        self.screen.blit(self.max_score_image,self.max_score_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.draw_lifes()





        pass