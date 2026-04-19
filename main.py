import pygame
import sys
import config
from snake import Snake
from food import spawn_food
from ai import astar
from ui import draw_cell, draw_menu, draw_game_over

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Snake AI Project")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

ai_button = pygame.Rect(config.WIDTH//2 - 120, config.HEIGHT//2 - 60, 240, 50)
manual_button = pygame.Rect(config.WIDTH//2 - 120, config.HEIGHT//2 + 20, 240, 50)

snake = Snake()
food = spawn_food(snake.body)
score = 0

mode = None
game_over = False

def reset_game():
    global snake, food, score, mode, game_over
    snake = Snake()
    food = spawn_food(snake.body)
    score = 0
    mode = None
    game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode is None and event.type == pygame.MOUSEBUTTONDOWN:
            if ai_button.collidepoint(event.pos):
                mode = "AI"
            elif manual_button.collidepoint(event.pos):
                mode = "MANUAL"

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.key == pygame.K_UP and snake.direction != (0, 1):
            snake.direction = (0, -1)
        elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
            snake.direction = (0, 1)
        elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
            snake.direction = (-1, 0)
        elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
            snake.direction = (1, 0)

    if mode is None:
        draw_menu(screen, font, ai_button, manual_button)
        pygame.display.flip()
        clock.tick(60)
        continue

    if game_over:
        draw_game_over(screen, font, score)
        pygame.display.flip()
        clock.tick(60)
        continue

    if mode == "AI":
        path = astar(snake.head(), food, snake.body)
        next_cell = path[0] if path else snake.head()
    else:
        next_cell = (snake.head()[0] + snake.direction[0],
                     snake.head()[1] + snake.direction[1])

    snake.move(next_cell)

    if snake.head() == food:
        score += 1
        food = spawn_food(snake.body)
    else:
        snake.shrink()

    if (snake.head()[0] < 0 or snake.head()[0] >= config.GRID_SIZE or
        snake.head()[1] < 0 or snake.head()[1] >= config.GRID_SIZE or
        snake.head() in snake.body[1:]):
        game_over = True

    screen.fill(config.BLACK)

    for x in range(config.GRID_SIZE):
        for y in range(config.GRID_SIZE):
            pygame.draw.rect(screen, (25, 25, 25),
                             (x * config.CELL_SIZE, y * config.CELL_SIZE,
                              config.CELL_SIZE, config.CELL_SIZE), 1)

    for i, (x, y) in enumerate(snake.body):
        color = config.GREEN if i == 0 else config.DARK_GREEN
        draw_cell(screen, x, y, color)

    fx, fy = food
    pygame.draw.circle(screen, config.RED,
                       (fx * config.CELL_SIZE + config.CELL_SIZE//2,
                        fy * config.CELL_SIZE + config.CELL_SIZE//2),
                       config.CELL_SIZE//2 - 3)

    screen.blit(font.render(f"Score: {score} | Mode: {mode}", True, config.WHITE),
                (10, 10))

    pygame.display.flip()
    clock.tick(12)