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

# Movement speed
MOVEMENT_SPEED = 20

# Green colours
LIGHT_GREEN = (162, 210, 73)
DARK_GREEN = (170, 216, 81)
SNAKE_COLOR = (172, 118, 235)


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
        """
        CODE THAT GENERATES THE GRID
        """
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


class Snake:
    """
    CODE FOR THE SNAKE
    """
    def __init__(self, snake_pos_x, snake_pos_y, change_x, change_y, snake_width, snake_height, snake_color):
        """
        TURNS THE __INIT__ FUNCTIONS INTO VARIABLES
        """
        self.snake_pos_x = snake_pos_x
        self.snake_pos_y = snake_pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.snake_width = snake_width
        self.snake_height = snake_height
        self.snake_color = snake_color

    def draw(self):
        """
        SETS THE SNAKE CUBE UP TO BE DRAWN
        """
        arcade.draw_rectangle_filled(self.snake_pos_x, self.snake_pos_y, self.snake_width,
                                     self.snake_height, self.snake_color)

    def update(self):
        """
        CHANGES THE SNAKE POSITION TO THE KEYBOARD LOCATIONS
        """
        self.snake_pos_y += self.change_y
        self.snake_pos_x += self.change_x


class MyGame(arcade.Window):
    """
    MAIN CODE FOR THE GAME
    """
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_mouse_visible(True)

        arcade.set_background_color(DARK_GREEN)

        self.grid = Grid(0, 0, SQUARE_WIDTH, SQUARE_HEIGHT, LIGHT_GREEN)
        self.snake = Snake(180, 180, 0, 0, SQUARE_WIDTH, SQUARE_HEIGHT, SNAKE_COLOR)

    def on_draw(self):
        """
        RENDERS THE OBJECTS
        """
        arcade.start_render()
        self.grid.draw()
        self.snake.draw()

    def update(self, delta_time):
        """
        MOVES THE NEW SNAKE OBJECT TO THE AREA
        """
        self.snake.update()

    def on_key_press(self, key, modifiers):
        """
        CODE GETS CALLED EACH TIME THE USER PRESSES A KEY
        """
        if key == arcade.key.A:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        CODE GETS CALLED EACH TIME THE USER RELEASES A KEY
        """
        if key == arcade.key.A or key == arcade.key.D:
            self.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.change_y = 0


def main():
    window = MyGame(WINDOW_WIDTH, WINDOW_HEIGHT, "Grid.exe")
    arcade.run()


main()
