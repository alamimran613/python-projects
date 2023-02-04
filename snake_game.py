import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (500, 500)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the clock for controlling the game's framerate
clock = pygame.time.Clock()

# Define the size of the snake's block
block_size = 10

# Define the font to be used for displaying the score
font = pygame.font.Font(None, 25)

# Define the colors to be used
white = (255, 255, 255)
red = (255, 0, 0)

# Define the initial position of the snake
snake_position = [100, 50]

# Define the initial position of the food
food_position = [random.randrange(1, (window_size[0] // block_size)) * block_size,
                 random.randrange(1, (window_size[1] // block_size)) * block_size]
food_spawned = True

# Define the initial direction of the snake
direction = 'right'

# Define the initial length of the snake
snake_body = [snake_position] * 5

# Define the initial score
score = 0

# Define the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change the direction of the snake based on the keys pressed by the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'up'
            if event.key == pygame.K_DOWN:
                direction = 'down'
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                direction = 'right'

    # Move the snake in the specified direction
    if direction == 'right':
        snake_position[0] += 10
    if direction == 'left':
        snake_position[0] -= 10
    if direction == 'up':
        snake_position[1] -= 10
    if direction == 'down':
        snake_position[1] += 10

    # Increase the length of the snake if it has reached the food
    if snake_position == food_position:
        food_spawned = False
        score += 1
        snake_body.append([0, 0])

    # Spawn a new piece of food if the current piece has been eaten
    if not food_spawned:
        food_position = [random.randrange(1, (window_size[0] // block_size)) * block_size,
                         random.randrange(1, (window_size[1] // block_size)) * block_size]
        food_spawned = True

    # Move the body of the snake
    for i in range(len(snake_body)
