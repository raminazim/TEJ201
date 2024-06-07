import pygame

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 2000, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Player Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load car images and resize them
car1_img = pygame.image.load('Culminating/car1.png')
car1_img = pygame.transform.scale(car1_img, (101, 38))
car2_img = pygame.image.load('Culminating/car2.png')
car2_img = pygame.transform.scale(car2_img, (101, 38))

# Initial positions of cars
car1_x, car1_y = 100, 200
car2_x, car2_y = 100, 300

# Obstacles
obstacle_positions = [400, 800, 1200, 1600]
obstacles = [{'x': pos, 'y': 0, 'speed': 1, 'direction': 1} for pos in obstacle_positions]

# Game loop control
running = True
winner = None

# Game loop
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        car1_x += 2

    if keys[pygame.K_RIGHT]:
        car2_x += 2

    # Update obstacle positions
    for obstacle in obstacles:
        obstacle['y'] += obstacle['speed'] * obstacle['direction']
        if obstacle['y'] <= 0 or obstacle['y'] >= SCREEN_HEIGHT - 50:
            obstacle['direction'] *= -1

        # Draw obstacles
        pygame.draw.rect(screen, RED, pygame.Rect(obstacle['x'], obstacle['y'], 50, 50))

        # Collision detection with cars
        if (car1_x < obstacle['x'] + 50 and car1_x + 101 > obstacle['x'] and
                car1_y < obstacle['y'] + 50 and car1_y + 38 > obstacle['y']):
            car1_x, car1_y = 100, 200

        if (car2_x < obstacle['x'] + 50 and car2_x + 101 > obstacle['x'] and
                car2_y < obstacle['y'] + 50 and car2_y + 38 > obstacle['y']):
            car2_x, car2_y = 100, 300

    # Draw cars
    screen.blit(car1_img, (car1_x, car1_y))
    screen.blit(car2_img, (car2_x, car2_y))

    # Check for winner
    if car1_x >= SCREEN_WIDTH:
        winner = "Player One"
    elif car2_x >= SCREEN_WIDTH:
        winner = "Player Two"

    # Display winner
    if winner:
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"{winner} wins!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()

pygame.quit()
