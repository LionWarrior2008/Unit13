from typing import TYPE_CHECKING
import json
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class GameStats():
    def __init__(self,game:'AlienInvasion'):
        self.game=game
        self.settings=game.settings
        self.max_score=0
        self.reset_stats()
        self.init_saved_scores()
    def init_saved_scores(self):
        self.path=self.settings.score_file
        if self.path.exists() and self.path.stat.__sizeof__()>0:
            contents=self.path.read_text()
            if not contents:
                print("File empty")
            scores=json.loads(contents)
            self.high_score=scores.get('high_score',0)
        else:
            self.high_score=0
            self.saves_scores()
    def saves_scores(self):
        scores={'high_score':self.high_score}
        contents=json.dumps(scores,indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError:
            print(f"File was not found try again")



    def reset_stats(self):
        self.ship_left=self.settings.ship_limit
        self.score=0
        self.level=1
    def update(self,collisions):
        self.update_score(collisions)
        self.update_max_score()
        self.update_High_score()
    def update_max_score(self):
        if self.score>self.max_score:
            self.max_score=self.score
        print(f"Max:{self.max_score}")
    def update_High_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            self.saves_scores()

    def update_score(self,collisions):
        for alien in collisions.values():
            self.score+=self.settings.alien_points
        print(f"Max:{self.max_score}")
    def update_level(self):
        self.level+=1
        print(self.level)



        pass