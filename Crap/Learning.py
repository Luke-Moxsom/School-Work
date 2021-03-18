import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class MyGame(arcade.Window):
    """
    MAIN CODE FOR OUR GAME
    """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Learing.exe")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """
        SETS UP THE GAME AND SPRITES
        """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()


def main():
    """
    MAIN FUNCTION
    """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()