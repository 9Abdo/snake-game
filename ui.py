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

def draw_menu(screen, font, ai_button, manual_button):
    screen.fill(config.BLACK)

    title = font.render("Choose Mode", True, config.WHITE)
    screen.blit(title, (config.WIDTH//2 - 60, config.HEIGHT//2 - 120))

    pygame.draw.rect(screen, config.BLUE, ai_button, border_radius=10)
    pygame.draw.rect(screen, config.GRAY, manual_button, border_radius=10)

    screen.blit(font.render("AI Mode", True, config.WHITE),
                (ai_button.x + 80, ai_button.y + 15))

    screen.blit(font.render("Manual Mode", True, config.WHITE),
                (manual_button.x + 50, manual_button.y + 15))

def draw_game_over(screen, font, score):
    screen.fill(config.BLACK)

    screen.blit(font.render("GAME OVER", True, (255, 0, 0)),
                (config.WIDTH//2 - 80, config.HEIGHT//2 - 60))

    screen.blit(font.render(f"Score: {score}", True, config.WHITE),
                (config.WIDTH//2 - 50, config.HEIGHT//2 - 20))

    screen.blit(font.render("Press R to Restart | Q to Quit", True, config.WHITE),
                (config.WIDTH//2 - 140, config.HEIGHT//2 + 20))