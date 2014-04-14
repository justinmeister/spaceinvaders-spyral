import spyral

WIDTH = 1200
HEIGHT = 900

WHITE = (255, 255, 255)
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


class Alien(spyral.Sprite):
    """
    Enemies player must destroy.
    """
    def __init__(self, scene, row, column):
        super(Alien, self).__init__(scene)
        self.image = spyral.Image(size=(ENEMYSIDE, ENEMYSIDE)).fill(RED)
        self.anchor = 'topleft'
        self.row = row
        self.column = column
        self.x = (column * (ENEMYGAP + ENEMYSIDE)) + XMARGIN
        self.y = (row * (ENEMYGAP + ENEMYSIDE)) + YMARGIN
        self.name = 'enemy'
        self.vectorx = 1
        self.time_offset = row * 3
        self.move_time = 30
        self.move_count = 0
        self.timer = spyral.director.get_tick() - self.time_offset

        spyral.event.register('director.update', self.update_alien)

    def update_alien(self, delta):
        current_time = spyral.director.get_tick()

        if (current_time - self.timer) > self.move_time:
            if self.move_count < 6:
                self.x += MOVEX * self.vectorx
                self.move_count += 1
            elif self.move_count >= 6:
                self.vectorx *= -1
                self.move_count = 0
                self.y += MOVEY
            self.timer = current_time


class Bullet(spyral.Sprite):
    """
    Projectile launched when player hits space.
    """
    def __init__(self, scene, x, y):
        super(Bullet, self).__init__(scene)
        self.image = spyral.Image(size=(5, 5)).fill(GREEN)
        self.anchor = 'midtop'
        self.y_vel = -900
        self.x = x
        self.y = y
        spyral.event.register('director.update', self.update_bullet)

    def update_bullet(self, delta):
        self.y += self.y_vel * delta

        self.check_if_off_screen()

    def check_if_off_screen(self):
        if self.y < 0:
            #self.kill()
            pass


class Player(spyral.Sprite):
    """
    Player controlled sprite.
    """
    def __init__(self, scene, side, collision_handler):
        super(Player, self).__init__(scene)
        width = 200
        height = 20
        self.game_scene = scene
        self.collision_handler = collision_handler
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
        spyral.event.register('input.keyboard.up.space', self.reset_gun)
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
            bullet = Bullet(self.game_scene, self.x, self.y)
            self.collision_handler.add_bullet(bullet)
            self.allow_shoot = False

    def reset_gun(self):
        self.allow_shoot = True

    def update(self, delta):
        self.x += self.x_vel * delta

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH