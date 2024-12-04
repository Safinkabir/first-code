import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Simple Jump Game")

# Player settings
player_x = 50
player_y = 500
player_width = 40
player_height = 60
player_vel = 5
is_jumping = False
jump_height = 10
jump_count = 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_vel
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()