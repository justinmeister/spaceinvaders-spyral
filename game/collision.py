import spyral
from . sprites import sprite


class CollisionHandler(object):
    """
    Handles collisions between bullets, aliens and blockers.
    """
    def __init__(self, scene):
        self.scene = scene
        self.player = None
        self.alien_list = []
        self.bullet_list = []
        self.sprites_to_kill = []
        spyral.event.register('director.update', self.update)

    def update(self):
        """
        Check if there is a collision.
        """
        self.check_for_bullet_and_alien_collision()
        self.check_if_bullet_off_screen()
        self.kill_dead_sprites()


        for bullet in self.bullet_list:
            if bullet.y < 0:
                bullet.kill()

    def check_for_bullet_and_alien_collision(self):
        for i, alien in enumerate(self.alien_list):
            for j, bullet in enumerate(self.bullet_list):
                if bullet.collide_sprite(alien):
                    self.make_explosion(alien.x, alien.y)
                    self.sprites_to_kill.append(alien)
                    self.sprites_to_kill.append(bullet)
                    self.alien_list.pop(i)
                    self.bullet_list.pop(j)


    def check_if_bullet_off_screen(self):
        for i, bullet in enumerate(self.bullet_list):
            if bullet.y < 0:
                self.sprites_to_kill.append(bullet)
                self.bullet_list.pop(i)


    def kill_dead_sprites(self):
        for sprite in self.sprites_to_kill:
            sprite.kill()

    def make_explosion(self, x, y):
        explosion = sprite.Explosion(x, y, self.scene)




    def add_bullet(self, bullet):
        """
        Add bullet to bullet_list.
        """
        self.bullet_list.append(bullet)

    def add_aliens(self, aliens):
        """
        Add alien to alien_list.
        """
        self.alien_list = aliens

    def add_player(self, player):
        """
        Add player to handler.
        """
        self.player = player