import pygame
import sys
import config

from snake import Snake
from food import spawn_food
from obstacles import spawn_obstacles
from problem_formulation import SnakeProblem

from ai.astar import astar
from ai.bfs import bfs
from ai.greedy import greedy

from ui import draw_menu, draw_game_over, draw_game, draw_ai_menu

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Snake AI Project")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

ai_button = pygame.Rect(config.WIDTH//2 - 120, config.HEIGHT//2 - 60, 240, 50)
manual_button = pygame.Rect(config.WIDTH//2 - 120, config.HEIGHT//2 + 20, 240, 50)

bfs_btn = astar_btn = greedy_btn = None

snake = Snake()
food = spawn_food(snake.body, [])
obstacles = spawn_obstacles(snake.body, food)

score = 0
mode = None
ai_mode = None
game_over = False


def reset_game():
    global snake, food, obstacles, score, mode, ai_mode, game_over
    snake = Snake()
    food = spawn_food(snake.body, [])
    obstacles = spawn_obstacles(snake.body, food)
    score = 0
    mode = None
    ai_mode = None
    game_over = False

def create_ai_buttons():
    bfs_btn = pygame.Rect(config.WIDTH//2 - 100, 200, 200, 50)
    astar_btn = pygame.Rect(config.WIDTH//2 - 100, 270, 200, 50)
    greedy_btn = pygame.Rect(config.WIDTH//2 - 100, 340, 200, 50)
    return bfs_btn, astar_btn, greedy_btn

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode is None and event.type == pygame.MOUSEBUTTONDOWN:
            if ai_button.collidepoint(event.pos):
                mode = "AI_MENU"
                bfs_btn, astar_btn, greedy_btn = create_ai_buttons()

            elif manual_button.collidepoint(event.pos):
                mode = "MANUAL"

        if mode == "AI_MENU" and event.type == pygame.MOUSEBUTTONDOWN:

            if bfs_btn.collidepoint(event.pos):
                ai_mode = "BFS"
                mode = "AI"

            elif astar_btn.collidepoint(event.pos):
                ai_mode = "ASTAR"
                mode = "AI"

            elif greedy_btn.collidepoint(event.pos):
                ai_mode = "GREEDY"
                mode = "AI"

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if mode == "MANUAL" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)

    if mode is None:
        draw_menu(screen, font, ai_button, manual_button)
        pygame.display.flip()
        clock.tick(60)
        continue
    if mode == "AI_MENU":
        draw_ai_menu(screen, font, bfs_btn, astar_btn, greedy_btn)
        pygame.display.flip()
        clock.tick(60)
        continue

    if game_over:
        draw_game_over(screen, font, score)
        pygame.display.flip()
        clock.tick(60)
        continue

    if mode == "AI":
        problem = SnakeProblem(snake, food, config.GRID_SIZE, obstacles)

        if ai_mode == "BFS":
            path = bfs(problem)
        elif ai_mode == "GREEDY":
            path = greedy(problem)
        else:
            path = astar(problem)

        next_cell = path[0] if path else snake.head()

    else:
        next_cell = (
            snake.head()[0] + snake.direction[0],
            snake.head()[1] + snake.direction[1]
        )

    snake.move(next_cell)

    if snake.head() == food:
        score += 1
        food = spawn_food(snake.body, obstacles)
    else:
        snake.shrink()
    if (
        snake.head()[0] < 0 or snake.head()[0] >= config.GRID_SIZE or
        snake.head()[1] < 0 or snake.head()[1] >= config.GRID_SIZE or
        snake.head() in snake.body[1:] or
        snake.head() in obstacles
    ):
        game_over = True

    draw_game(screen, snake, food, obstacles, score, mode, ai_mode, font)

    pygame.display.flip()
    clock.tick(10)