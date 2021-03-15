import arcade

WINDOW_WIDTH = 740
WINDOW_HEIGHT = 740
dark_green = (170, 216, 81)
light_green = (162, 210, 73)
snake_color = (72, 118, 235)


def square(square_x, square_y, square_width, square_height, square_color):
    """ Code that sets up the squares for generation """
    arcade.draw_rectangle_filled(square_x, square_y, square_width, square_height, square_color)


def generate_grid():
    """ Code that generates the grid """
    y_offset = -10
    for a in range(20):
        # Line 1
        # Adds offset to the x position of the squares
        x_offset = 10
        for b in range(1):
            # Adds offset to the y position of the squares
            y_offset += 20
        for c in range(20):
            # Prints a row of squares(5 squares along the x)
            square(x_offset, y_offset, 20, 20, dark_green)
            for d in range(1):
                # Adds x offset for the next line of squares on the y axis
                x_offset += 40
        # Line 2 (needs 2 lines because the offset of each line)
        # Adds offset to the x position of the squares
        x_offset = 30
        for e in range(1):
            # Adds offset to the y position of the squares
            y_offset += 20
        for f in range(20):
            # Prints a row of squares(5 squares along the x)
            square(x_offset, y_offset, 20, 20, dark_green)
            for g in range(1):
                # Adds x offset for the next line of squares on the y axis
                x_offset += 40


def apple():
    """ Draws an apple """
    arcade.draw_circle_filled(230, 490, 9.5, (231, 71, 29))


def snake(snake_x, snake_y, snake_scale_x, snake_scale_y, snake_color):
    """ Code that sets up the snake part to be drawn """
    arcade.draw_rectangle_filled(snake_x, snake_y, snake_scale_x, snake_scale_y, snake_color)


def on_draw(delta_time):
    """ Draw everything every frame(we chose in on_draw.schedule(e.g I chose 1/3 so every 1/3 of a second a frame is
    drawn)). """
    # draws all our objects
    arcade.start_render()

    generate_grid()
    apple()
    snake(on_draw.snake_part_x, on_draw.snake_part_y, 20, 20, snake_color)
    snake(on_draw.snake_part2_x, on_draw.snake_part2_y, 20, 20, snake_color)
    snake(on_draw.snake_part3_x, on_draw.snake_part3_y, 20, 20, snake_color)
    snake(on_draw.snake_part4_x, on_draw.snake_part4_y, 20, 20, snake_color)
    snake(on_draw.snake_part5_x, on_draw.snake_part5_y, 20, 20, snake_color)
    snake(on_draw.snake_part6_x, on_draw.snake_part6_y, 20, 20, snake_color)


    if on_draw.snake_part_x <= 230:
        snake(on_draw.snake_part6_x + 20, on_draw.snake_part6_y, 20, 20, snake_color)


    """ If statements that will make snake part one move """
    if on_draw.snake_part_x >= 550:
        on_draw.snake_part_x -= 20

    elif on_draw.snake_part_x <= 550:
        on_draw.snake_part_y += 20
        if on_draw.snake_part_y >= 500:
            on_draw.snake_part_y -= 20
            on_draw.snake_part_x -= 20
            if on_draw.snake_part_x <= 180:
                on_draw.snake_part_x += 20

    """ If statements that will make snake part two move """
    if on_draw.snake_part2_x >= 550:
        on_draw.snake_part2_x -= 20

    elif on_draw.snake_part2_x <= 550:
        on_draw.snake_part2_y += 20
        if on_draw.snake_part2_y >= 500:
            on_draw.snake_part2_y -= 20
            on_draw.snake_part2_x -= 20
            if on_draw.snake_part2_x <= 200:
                on_draw.snake_part2_x += 20

    """ If statements that will make snake part three move """
    if on_draw.snake_part3_x >= 550:
        on_draw.snake_part3_x -= 20

    elif on_draw.snake_part3_x <= 550:
        on_draw.snake_part3_y += 20
        if on_draw.snake_part3_y >= 500:
            on_draw.snake_part3_y -= 20
            on_draw.snake_part3_x -= 20
            if on_draw.snake_part3_x <= 220:
                on_draw.snake_part3_x += 20

    """ If statements that will make snake part four move """
    if on_draw.snake_part4_x >= 550:
        on_draw.snake_part4_x -= 20

    elif on_draw.snake_part4_x <= 550:
        on_draw.snake_part4_y += 20
        if on_draw.snake_part4_y >= 500:
            on_draw.snake_part4_y -= 20
            on_draw.snake_part4_x -= 20
            if on_draw.snake_part4_x <= 240:
                on_draw.snake_part4_x += 20

    """ If statements that will make snake part five move """
    if on_draw.snake_part5_x >= 550:
        on_draw.snake_part5_x -= 20

    elif on_draw.snake_part5_x <= 550:
        on_draw.snake_part5_y += 20
        if on_draw.snake_part5_y >= 500:
            on_draw.snake_part5_y -= 20
            on_draw.snake_part5_x -= 20
            if on_draw.snake_part5_x <= 260:
                on_draw.snake_part5_x += 20

    """ If statements that will make snake part six move """
    if on_draw.snake_part6_x >= 550:
        on_draw.snake_part6_x -= 20

    elif on_draw.snake_part6_x <= 550:
        on_draw.snake_part6_y += 20
        if on_draw.snake_part6_y >= 500:
            on_draw.snake_part6_y -= 20
            on_draw.snake_part6_x -= 20
            if on_draw.snake_part6_x <= 280:
                on_draw.snake_part6_x += 20


# Sets a initial value to on_draw.snake_part_x(this is the starting position of the snake)
on_draw.snake_part_x = 570
on_draw.snake_part_y = 130
on_draw.snake_part2_x = 590
on_draw.snake_part2_y = 130
on_draw.snake_part3_x = 610
on_draw.snake_part3_y = 130
on_draw.snake_part4_x = 630
on_draw.snake_part4_y = 130
on_draw.snake_part5_x = 650
on_draw.snake_part5_y = 130
on_draw.snake_part6_x = 670
on_draw.snake_part6_y = 130


def main():
    """ Main code the calls all the rest of the code """
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Snake.exe")
    # Set the window background colour
    arcade.set_background_color(light_green)

    # Calls the on_draw method every 1/3(20 seconds) of a second
    arcade.schedule(on_draw, 1/3)
    # Keeps the window open until closed by the user
    arcade.run()


main()
