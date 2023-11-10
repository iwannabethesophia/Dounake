import pygame
import random

# Create snake
snake1 = [(50, 50), (40, 50), (30, 50)]
snake2 = [(350, 350), (360, 350), (370, 350)]
snake1_direction = 'RIGHT'
snake2_direction = 'LEFT'
width = 400
height = 400

# Create apple
apples = []
for _ in range(5):
    x = random.randrange(1, (width // 10)) * 10
    y = random.randrange(1, (height // 10)) * 10
    apples.append((x, y))

# Check collision of first player
for segment in snake2[1:]:
    if snake1[0] == segment:
        running = False

    # Check collision of 2rd player
for segment in snake1[1:]:
    if snake2[0] == segment:
        running = False
    
    # Implement collision with screen 
if (snake1[0][0] >= width or snake1[0][0] < 0 or snake1[0][1] >= height or snake1[0][1] < 0) or (snake2[0][0] >= width or snake2[0][0] < 0 or snake2[0][1] >= height or snake2[0][1] < 0):
    running = False

# Check collision between apple with first player
for apple in apples:
    if snake1[0] == apple:
        apples.remove(apple)
        x = random.randrange(1, (width // 10)) * 10
        y =apples.append((x, y))
            
# check collision between apple with 2rd player
if snake2[0] == apple:
    apples.remove(apple)
    x = random.randrange(1, (width // 10)) * 10
    y = random.randrange(1, (height // 10)) * 10
    apples.append((x, y))
            








