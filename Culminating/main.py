import pygame
import time

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cross the Road")

# Colors
WHITE = (255, 255, 255)
LGREEN = (154, 205, 50)
LBLUE = (135, 206, 250)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Load images
player_img = pygame.image.load('Culminating/player.png')
car_gold_img = pygame.image.load('Culminating/car_gold.png')
car_blue_img = pygame.image.load('Culminating/car_blue.png')
car_green_img = pygame.image.load('Culminating/car_green.png')
bg_img = pygame.image.load('Culminating/background.png')
road_img = pygame.image.load('Culminating/road.png')

# Scale images if necessary
player_img = pygame.transform.scale(player_img, (30, 30))
car_gold_img = pygame.transform.scale(car_gold_img, (101, 38))
car_blue_img = pygame.transform.scale(car_blue_img, (101, 38))
car_green_img = pygame.transform.scale(car_green_img, (101, 38))
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale background image to cover the screen

# Font
font = pygame.font.SysFont("Bernard MT", 37)

# Game variables
strScoreCount = 0
intRectX, intRectY = 400, 500
intCarSpeedONE = 25
intCarSpeedTWO = 37.5
intCarSpeedTHREE = 50

intCircleXONE, intCircleYONE = -50, 375
intCircleXTWO, intCircleYTWO = -50, 275
intCircleXTHREE, intCircleYTHREE = -50, 175

# Timer variables
start_time = None
elapsed_time = 0
timer_font = pygame.font.SysFont("Bernard MT", 25)

# Previous game score
prev_score = 0

# Game loop control
running = True
playing = False
timer = pygame.time.Clock()

def draw_menu():
    screen.fill(LGREEN)
    title_text = font.render("Cross the Road", True, BLACK)
    play_text = font.render("Play", True, BLACK)
    instruction_text = font.render("Try to cross the road using WASD or arrow keys. Get the highest score possible in 60 seconds", True, BLACK)
    prev_score_text = font.render("Previous Score: " + str(prev_score), True, BLACK)

    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 150))
    screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, 250))
    screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, 350))
    screen.blit(prev_score_text, (SCREEN_WIDTH // 2 - prev_score_text.get_width() // 2, 400))

def draw_game():
    screen.blit(bg_img, (0, 0))  # Draw background image covering the whole screen

    # Draw road
    screen.blit(road_img, (0, 200))

    # Draw cars
    screen.blit(car_gold_img, (intCircleXONE, intCircleYONE))
    screen.blit(car_blue_img, (intCircleXTWO, intCircleYTWO))
    screen.blit(car_green_img, (intCircleXTHREE, intCircleYTHREE))

    # Draw player
    screen.blit(player_img, (intRectX, intRectY))

    # Render score
    score_text = font.render("Score: " + str(strScoreCount), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Render timer
    if start_time is not None:
        elapsed_time = pygame.time.get_ticks() - start_time
        seconds = (60000 - elapsed_time) // 1000
        timer_text = timer_font.render("Time: " + str(seconds) + "s", True, WHITE)
        screen.blit(timer_text, (SCREEN_WIDTH - timer_text.get_width() - 10, 10))

def update_game():
    global intCircleXONE, intCircleXTWO, intCircleXTHREE
    global intRectX, intRectY, strScoreCount, start_time

    if start_time is None:
        start_time = pygame.time.get_ticks()

    # Update car positions
    intCircleXONE += intCarSpeedONE
    intCircleXTWO += intCarSpeedTWO
    intCircleXTHREE += intCarSpeedTHREE

    if intCircleXONE > 800:
        intCircleXONE = -50
    if intCircleXTWO > 800:
        intCircleXTWO = -50
    if intCircleXTHREE > 800:
        intCircleXTHREE = -50

    # Player movement
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_a] or key_input[pygame.K_LEFT]:
        intRectX -= 8  # Increase the player's leftward movement speed
    if key_input[pygame.K_d] or key_input[pygame.K_RIGHT]:
        intRectX += 8  # Increase the player's rightward movement speed
    if key_input[pygame.K_w] or key_input[pygame.K_UP]:
        intRectY -= 8  # Increase the player's upward movement speed
    if key_input[pygame.K_s] or key_input[pygame.K_DOWN]:
        intRectY += 8  # Increase the player's downward movement speed

    # Score update
    if intRectY < -50:
        intRectY = 500
        strScoreCount += 1

    # Collision detection
    player_rect = pygame.Rect(intRectX, intRectY, 30, 30)
    car_one_rect = pygame.Rect(intCircleXONE, intCircleYONE, 50, 30)
    car_two_rect = pygame.Rect(intCircleXTWO, intCircleYTWO, 50, 30)
    car_three_rect = pygame.Rect(intCircleXTHREE, intCircleYTHREE, 50, 30)

    if player_rect.colliderect(car_one_rect) or player_rect.colliderect(car_two_rect) or player_rect.colliderect(car_three_rect):
        intRectX = 400
        intRectY = 500

    if intRectY > 600:
        intRectY = 500
    if intRectX < 0:
        intRectX = 800
    if intRectX > 800:
        intRectX = 0

while running:
    screen.fill(LGREEN)

    if not playing:
        draw_menu()
        start_time = None  # Reset timer when not playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if SCREEN_WIDTH // 2 - 50 < mouse_x < SCREEN_WIDTH // 2 + 50 and 250 < mouse_y < 300:
                    playing = True
    else:
        draw_game()
        update_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.display.flip()
    timer.tick(30)

    if start_time is not None and pygame.time.get_ticks() - start_time >= 60000:  # Check if 60 seconds have elapsed
        playing = False
        prev_score = strScoreCount

pygame.quit()
