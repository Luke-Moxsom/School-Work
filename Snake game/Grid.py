import arcade

# Change these to change the x/y size of the screen
SCREEN_SIZE_x = 600
SCREEN_SIZE_y = 600

# Square width/height
SQUARE_WIDTH = 40
SQUARE_HEIGHT = 40

# Column/row
COLUMN = 8
ROW = 8

# Screen width/height
WINDOW_WIDTH = SCREEN_SIZE_x
WINDOW_HEIGHT = SCREEN_SIZE_y

# Green colours
LIGHT_GREEN = (162, 210, 73)
DARK_GREEN = (170, 216, 81)


class Grid:
    """
    CODE FOR THE GRID SETUP
    """
    def __init__(self, square_x, square_y, square_width, square_height, square_color):

        # Converts the init functions into variables
        self.square_x = square_x
        self.square_y = square_y
        self.square_width = square_width
        self.square_height = square_height
        self.square_color = square_color

    def draw(self):

        """ Code that generates the grid """
        y_offset = -SQUARE_HEIGHT / 2
        for a in range(COLUMN):
            # Line 1
            # Adds offset to the x position of the squares
            x_offset = SQUARE_WIDTH / 2
            for b in range(1):
                # Adds offset to the y position of the squares
                y_offset += SQUARE_HEIGHT
            for c in range(ROW):
                # Prints a row of squares(5 squares along the x)
                arcade.draw_rectangle_filled(self.square_x + x_offset, self.square_y + y_offset,
                                             self.square_width, self.square_height, self.square_color)
                for d in range(1):
                    # Adds x offset for the next line of squares on the y axis
                    x_offset += SQUARE_WIDTH * 2
            # Line 2 (needs 2 lines because the offset of each line)
            # Adds offset to the x position of the squares
            x_offset = SQUARE_WIDTH + SQUARE_WIDTH / 2
            for e in range(1):
                # Adds offset to the y position of the squares
                y_offset += SQUARE_HEIGHT
            for f in range(ROW):
                # Prints a row of squares(5 squares along the x)
                arcade.draw_rectangle_filled(self.square_x + x_offset, self.square_y + y_offset,
                                             self.square_width, self.square_height, self.square_color)
                for g in range(1):
                    # Adds x offset for the next line of squares on the y axis
                    x_offset += SQUARE_WIDTH * 2


class MyGame(arcade.Window):
    """
    MAIN CODE FOR THE GAME
    """
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(True)

        arcade.set_background_color(DARK_GREEN)

        self.grid = Grid(0, 0, SQUARE_WIDTH, SQUARE_HEIGHT, LIGHT_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.grid.draw()


def main():
    window = MyGame(WINDOW_WIDTH, WINDOW_HEIGHT, "Grid.exe")
    arcade.run()


main()
