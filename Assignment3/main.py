import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving shapes")

# Rectangle properties
rect_x = 200
rect_y = 200
rect_width = 60
rect_height = 20
rect_vel = 10

# Circle properties
circle_x = 100
circle_y = 100
circle_width = 60
circle_height = 20
circle_vel = 10

run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # Rectangle movement (arrow keys)
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_vel
    if keys[pygame.K_RIGHT] and rect_x < 500 - rect_width:
        rect_x += rect_vel
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_vel
    if keys[pygame.K_DOWN] and rect_y < 500 - rect_height:
        rect_y += rect_vel
    
    # Circle movement (WASD keys)
    if keys[pygame.K_a] and circle_x > 0:
        circle_x -= circle_vel
    if keys[pygame.K_d] and circle_x < 500 - circle_width:
        circle_x += circle_vel
    if keys[pygame.K_w] and circle_y > 0:
        circle_y -= circle_vel
    if keys[pygame.K_s] and circle_y < 500 - circle_height:
        circle_y += circle_vel

    # Redraw window
    win.fill((0, 0, 0))  # Clear screen
    pygame.draw.rect(win, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))  # Draw rectangle
    pygame.draw.ellipse(win, (0, 0, 255), (circle_x, circle_y, circle_width, circle_height))  # Draw circle
    pygame.display.update()

pygame.quit()