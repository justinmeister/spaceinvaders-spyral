import spyral


class CollisionHandler(object):
    """
    Handles collisions between bullets, aliens and blockers.
    """
    def __init__(self):
        self.player = None
        self.alien_list = []
        self.bullet_list = []
        self.bullets_to_kill = []
        self.aliens_to_kill = []
        spyral.event.register('director.update', self.update)

    def update(self):
        """
        Check if there is a collision.
        """
        if len(self.alien_list) > 0 and len(self.bullet_list) > 0:
            self.check_for_bullet_and_alien_collision()


        for bullet in self.bullet_list:
            if bullet.y < 0:
                bullet.kill()

    def check_for_bullet_and_alien_collision(self):
        for i, alien in enumerate(self.alien_list):
            for j, bullet in enumerate(self.bullet_list):
                if bullet.collide_sprite(alien):
                    bullet.kill()
                    alien.kill()



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