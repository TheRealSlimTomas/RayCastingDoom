from sprite_object import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list []
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.anim_sprite_path = "resources/sprites/animated_sprites/"
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprites(game))

    def update(self):
        [sprite_update() for sprite in self.sprite_list]


    def add_sprites(self, sprites):
        self.sprite_list.append(sprites)