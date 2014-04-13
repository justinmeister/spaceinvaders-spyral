import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
GREEN = (60, 179, 113)


class Bullet(spyral.Sprite):
    def __init__(self, scene, x, y):
        super(Bullet, self).__init__(scene)
        self.image = spyral.Image(size=(5, 5)).fill(GREEN)
        self.anchor = 'midtop'
        self.y_vel = -800
        self.x = x
        self.y = y
        spyral.event.register('director.update', self.update)

    def update(self, delta):
        self.y += self.y_vel * delta



class Player(spyral.Sprite):
    def __init__(self, scene, side):
        super(Player, self).__init__(scene)
        width = 200
        height = 20
        self.game_scene = scene
        self.image = spyral.Image(size=(width, height)).fill(GREEN)
        self.anchor = 'midtop'
        self.x_vel = 0
        self.x = WIDTH / 2
        self.y = HEIGHT - 40
        self.side = side
        self.moving = False
        self.allow_shoot = True

        spyral.event.register("input.keyboard.down.right", self.move_right)
        spyral.event.register("input.keyboard.down.left", self.move_left)
        spyral.event.register('input.keyboard.down.space', self.shoot)
        spyral.event.register('input.keyboard.up.space', self.allow_shoot)
        spyral.event.register("input.keyboard.up.right", self.stop_move)
        spyral.event.register("input.keyboard.up.left", self.stop_move)
        spyral.event.register("director.update", self.update)
        
    def move_right(self):
        self.x_vel = 500

    def move_left(self):
        self.x_vel = -500

    def stop_move(self):
        self.x_vel = 0

    def shoot(self):
        if self.allow_shoot:
            Bullet(self.game_scene, self.x, self.y)
            self.allow_shoot = False

    def allow_shoot(self):
        self.allow_shoot = True

    def _reset(self):
        self.y = HEIGHT/2
        
    def update(self, delta):
        self.x += self.x_vel * delta
                
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            
        #self.pos == getattr(r, self.anchor)


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill(BG_COLOR)
        
        self.left_paddle = Player(self, 'left')

        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("director.update", self.update)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        
    def update(self, delta):
        pass
    