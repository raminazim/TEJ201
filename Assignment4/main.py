import pygame
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LGREEN = (154, 205, 50)
GRAY = (128, 128, 128)
YELLOW =(255,255,0)
LBLUE =(135,206,250)
pygame.init()
screen = pygame.display.set_mode((800, 600))

strScoreCount = 0
intCircleXONE = 800
intCircleYONE = 375
intCircleXTWO = 800
intCircleYTWO = 275
intCircleXTHREE = 800
intCircleYTHREE = 175

intCarSpeedONE = 7
intCarSpeedTWO = 9
intCarSpeedTHREE = 12

intRectX = 400
intRectY = 500

font = pygame.font.SysFont("Bernard MT", 37)

running = True
timer = pygame.time.Clock()

while running:
  screen.fill(LGREEN)

  # Draw sky and ground
  pygame.draw.rect(screen, LBLUE, pygame.Rect(0, 0, 800, 100))
  pygame.draw.rect(screen, LGREEN, pygame.Rect(0, 100, 800, 500))

  # Draw sun
  pygame.draw.circle(screen, YELLOW, (100, 100), 50)


  # Draw road
  pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 200, 800, 200))

  # Draw cars
  pygame.draw.rect(screen, RED, pygame.Rect(intCircleXONE, intCircleYONE, 50, 30))
  pygame.draw.rect(screen, BLUE, pygame.Rect(intCircleXTWO, intCircleYTWO, 50, 30))
  pygame.draw.rect(screen, GREEN, pygame.Rect(intCircleXTHREE, intCircleYTHREE, 50, 30))

  # Draw player
  pygame.draw.rect(screen, BLACK, pygame.Rect(intRectX, intRectY, 30, 30))

  # Update car positions
  intCircleXONE -= intCarSpeedONE
  intCircleXTWO -= intCarSpeedTWO
  intCircleXTHREE -= intCarSpeedTHREE

  if intCircleXONE < -50:
      intCircleXONE = 800
  if intCircleXTWO < -50:
      intCircleXTWO = 800
  if intCircleXTHREE < -50:
      intCircleXTHREE = 800

  # Player movement
  key_input = pygame.key.get_pressed()
  if key_input[pygame.K_LEFT]:
      intRectX -= 5
  if key_input[pygame.K_RIGHT]:
      intRectX += 5
  if key_input[pygame.K_UP]:
      intRectY -= 5
  if key_input[pygame.K_DOWN]:
      intRectY += 5

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

  # Event handling
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  # Render score
  score_text = font.render("Score: " + str(strScoreCount), True, WHITE)
  screen.blit(score_text, (10, 10))

  pygame.display.set_caption(str(strScoreCount))

  timer.tick(60)
  pygame.display.update()

pygame.quit()