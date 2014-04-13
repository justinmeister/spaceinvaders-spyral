import spyral


class CollisionHandler(object):
    """
    Handles collisions between bullets, aliens and blockers.
    """
    def __init__(self):
        self.player = None
        self.alien_list = []
        self.bullet_list = []
        spyral.event.register('director.update', self.update)

    def update(self):
        """
        Check if there is a collision.
        """
        for alien in self.alien_list:
            for bullet in self.bullet_list:
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