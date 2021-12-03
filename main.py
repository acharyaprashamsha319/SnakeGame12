import turtle
import random
W = 600
H = 600
FOOD_SIZE = 15
Delay= 200 # milliseconds

offsets = {
    "up": (0, 25),
    "down": (0, -25),
    "left": (-25, 0),
    "right": (25, 0)
}

def reset():
    global snake, snake_direction, food_pos, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    # screen.update() Only needed if we are fussed about drawing food before next call to `draw_snake()`.
    move_snake()

def move_snake():
    global snake_direction

    #  Next position for head of snake.
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:  # Or collision with walls?
        reset()
    else:
        # No self-collision so we can continue moving the snake.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        #  Allow screen wrapping
        if snake[-1][0] > W/ 2:
            snake[-1][0] -= W
        elif snake[-1][0] < - W / 2:
            snake[-1][0] += W
        elif snake[-1][1] > H / 2:
            snake[-1][1] -= H
        elif snake[-1][1] < -H / 2:
            snake[-1][1] += H

        # Clear previous snake stamps
        pen.clearstamps()

        # Draw snake
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Refresh screen
        screen.update()

        # Rinse and repeat
        turtle.ontimer(move_snake, Delay)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(- W / 2 + FOOD_SIZE, W / 2 - FOOD_SIZE)
    y = random.randint(- H / 2 + FOOD_SIZE, H / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Screen
screen = turtle.Screen()
screen.setup(W, H)
screen.title("Snake master play and have fanda")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

# Pen
pen = turtle.Turtle("square")
pen.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.shapesize(FOOD_SIZE / 20)  # Default size of turtle "square" shape is 20.
food.penup()

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Let's go
reset()
turtle.done()