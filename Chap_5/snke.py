import pygame
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Chasing Mouse")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

# Snake settings
snake = []
segment_size = 15
snake_length = 30

# Starting position
head_x = WIDTH // 2
head_y = HEIGHT // 2

for i in range(snake_length):
    snake.append((head_x - i * segment_size, head_y))

speed = 4

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Direction toward mouse
    dx = mouse_x - head_x
    dy = mouse_y - head_y

    distance = math.hypot(dx, dy)

    if distance > 1:
        dx /= distance
        dy /= distance

        head_x += dx * speed
        head_y += dy * speed

    # Add new head
    snake.insert(0, (head_x, head_y))

    # Remove tail
    if len(snake) > snake_length:
        snake.pop()

    # Draw
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.circle(
            screen,
            WHITE,
            (int(segment[0]), int(segment[1])),
            segment_size
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()