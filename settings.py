from pathlib import Path
class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.difficutly_scale=2
        self.botton_w=200
        self.botton_h=50
        self.botton_color=(0,135,50)
        self.text_color=(0,0,0)
        self.font_style=Path.cwd()/'Tektur_Condensed-Black.ttf'
        self.botton_font_size=48
        self.hud_font_size=20        
        self.fleet_direction = -1
        self.score_file=Path.cwd()/'scores.json'
    def intialise_dynamic_settings(self):
        self.ship_speed=4
        self.ship_limit = 3
        self.bullet_speed = 5.0
        self.alien_speed=2.0
        self.fleet_move = 5
        self.bullet_width = 15
        self.bullet_height = 3
        self.alien_points=50
    def increase_diff(self):
        self.alien_speed *= self.difficutly_scale
        self.bullet_speed *= self.difficutly_scale
        self.ship_speed *= self.difficutly_scale


