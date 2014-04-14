import spyral
from .sprites import sprite
from . import collision

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
GREEN = (60, 179, 113)
RED = (255, 0, 0)
BLACKBLUE = (19, 15, 48)
BG_COLOR = BLACKBLUE

ENEMYGAP = 30
XMARGIN = 175
YMARGIN = 100
MOVEX = 15
MOVEY = 20
ENEMYSIDE = 50


class Level1(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill(BG_COLOR)

        self.collision_handler = collision.CollisionHandler(self)
        self.player = sprite.Player(self, 'left', self.collision_handler)
        self.alien_list = self.make_aliens(6, 3)
        self.collision_handler.add_player(self.player)
        self.collision_handler.add_aliens(self.alien_list)

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("director.update", self.update)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        
    def update(self, delta):
        pass

    def make_aliens(self, columns, rows):
        """
        Make aliens and send them to collision handler.
        """
        alien_list = []

        for column in range(columns):
            for row in range(rows):
                alien = sprite.Alien(self, row, column)
                alien_list.append(alien)

        return alien_list

