import pygame
import config

def draw_cell(screen, x, y, color):
    pygame.draw.rect(
        screen,
        color,
        (x * config.CELL_SIZE, y * config.CELL_SIZE,
         config.CELL_SIZE, config.CELL_SIZE),
        border_radius=6
    )

def draw_grid(screen):
    for x in range(config.GRID_SIZE):
        for y in range(config.GRID_SIZE):
            pygame.draw.rect(
                screen,
                (25, 25, 25),
                (x * config.CELL_SIZE, y * config.CELL_SIZE,
                 config.CELL_SIZE, config.CELL_SIZE),
                1
            )
def draw_menu(screen, font, ai_button, manual_button):
    screen.fill(config.BLACK)

    title = font.render("Choose Mode", True, config.WHITE)
    screen.blit(title, (config.WIDTH//2 - 60, 80))

    pygame.draw.rect(screen, config.BLUE, ai_button, border_radius=10)
    pygame.draw.rect(screen, config.GRAY, manual_button, border_radius=10)

    screen.blit(font.render("AI Mode", True, config.WHITE),
                (ai_button.x + 80, ai_button.y + 15))

    screen.blit(font.render("Manual Mode", True, config.WHITE),
                (manual_button.x + 50, manual_button.y + 15))

def draw_ai_menu(screen, font, bfs_btn, astar_btn, greedy_btn):
    screen.fill(config.BLACK)

    title = font.render("Choose AI Algorithm", True, config.WHITE)
    screen.blit(title, (config.WIDTH//2 - 120, 100))

    pygame.draw.rect(screen, config.bfs_btn, bfs_btn, border_radius=10)
    pygame.draw.rect(screen, config.astar_btn, astar_btn, border_radius=10)
    pygame.draw.rect(screen, config.greedy_btn, greedy_btn, border_radius=10)

    screen.blit(font.render("BFS", True, config.BLACK),
                (bfs_btn.x + 80, bfs_btn.y + 15))

    screen.blit(font.render("A*", True, config.BLACK),
                (astar_btn.x + 90, astar_btn.y + 15))

    screen.blit(font.render("GREEDY", True, config.BLACK),
                (greedy_btn.x + 60, greedy_btn.y + 15))

def draw_game_over(screen, font, score):
    screen.fill(config.BLACK)

    screen.blit(font.render("GAME OVER", True, (255, 0, 0)),
                (config.WIDTH//2 - 80, config.HEIGHT//2 - 60))

    screen.blit(font.render(f"Score: {score}", True, config.WHITE),
                (config.WIDTH//2 - 50, config.HEIGHT//2 - 20))

    screen.blit(font.render("Press R to Restart | Q to Quit", True, config.WHITE),
                (config.WIDTH//2 - 160, config.HEIGHT//2 + 20))

def draw_game(screen, snake, food, obstacles, score, mode, ai_mode, font):
    screen.fill(config.BLACK)

    draw_grid(screen)
    for (x, y) in obstacles:
        draw_cell(screen, x, y, config.BLUE)

    # snake
    for i, (x, y) in enumerate(snake.body):
        color = config.GREEN if i == 0 else config.DARK_GREEN
        draw_cell(screen, x, y, color)

    fx, fy = food
    pygame.draw.circle(
        screen,
        config.RED,
        (fx * config.CELL_SIZE + config.CELL_SIZE//2,
         fy * config.CELL_SIZE + config.CELL_SIZE//2),
        config.CELL_SIZE//2 - 3
    )

    screen.blit(
        font.render(f"Score: {score} | Mode: {mode} | AI: {ai_mode}",
                    True, config.WHITE),
        (10, 10)
    )