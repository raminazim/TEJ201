import pygame
import time 

pygame.init()


screen_width, screen_height = 2000, 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Two Player Racing Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the images for the two cars and scale them to a specified size
car1_img = pygame.image.load('Culminating/car1.png')
car1_img = pygame.transform.scale(car1_img, (100, 40))

car2_img = pygame.image.load('Culminating/car2.png')
car2_img = pygame.transform.scale(car2_img, (100, 40))

# Set the initial positions of the two cars
car1_x, car1_y = 100, 200
car2_x, car2_y = 100, 300

# Define the positions of obstacles along the x-axis and set their properties
ObstaclePositions = [400, 800, 1200, 1600]
Obstacles = [{'x': pos, 'y': 0, 'speed': 1, 'direction': 1} for pos in ObstaclePositions]

running = True  # Variable to control the main game loop
game_state = "start"  # Set the initial game state to start
winner = None  # Variable to store the winner

# Function to reset the positions of the cars
def reset_positions():
    global car1_x, car1_y, car2_x, car2_y
    car1_x, car1_y = 100, 200
    car2_x, car2_y = 100, 300

# Main game loop
while running:
    screen.fill(WHITE)  # Fill the screen with white color

    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # If the quit event is triggered, exit the loop
            running = False

    if game_state == "start":  # If the game state is start
        font = pygame.font.SysFont(None, 48)  # Create a font object
        # Show the instructions text
        instructions = font.render("Press SPACE to start the game, Player One Uses 'D', Player Two Uses Arrow Key", True, BLACK)
        # Display the instructions text at the center of the screen
        screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, screen_height // 2 - instructions.get_height() // 2))
        pygame.display.flip()  # Update the display

        keys = pygame.key.get_pressed()  # Get the state of all keyboard input
        if keys[pygame.K_SPACE]:  # If space is pressed
            game_state = "countdown"  # Change the game state to countdown
            countdown_start_time = time.time()  # Record the start time of the countdown

    elif game_state == "countdown":  # If the game state is countdown
        elapsed_time = time.time() - countdown_start_time  # Calculate the elapsed time
        countdown = max(0, 3 - int(elapsed_time))  # Calculate the countdown value (3 to 0)

        font = pygame.font.SysFont(None, 48)  # Create a font object
        # Render the countdown text
        countdown_display = font.render(f"{countdown}", True, BLACK)
        # Display the countdown text at the center of the screen
        screen.blit(countdown_display, (screen_width // 2 - countdown_display.get_width() // 2, screen_height // 2 - countdown_display.get_height() // 2))
        pygame.display.flip()  # Update the display

        if countdown <= 0:  # If the countdown reaches zero
            reset_positions()  # Reset the positions of the cars to prevent cheating
            game_state = "play"  # Change the game state to play

    elif game_state == "play":  # If the game state is play
        keys = pygame.key.get_pressed()  # Get the state of all keyboard buttons

        if keys[pygame.K_d]:  # If the 'D' key is pressed
            car1_x += 2  # Move Car1

        if keys[pygame.K_RIGHT]:  # If the right arrow key is pressed
            car2_x += 2  # Move Car2

        for Obstacle in Obstacles:  # For each obstacle
            Obstacle['y'] += Obstacle['speed'] * Obstacle['direction']  # Move the obstacle
            if Obstacle['y'] <= 0 or Obstacle['y'] >= screen_height - 50:  # If the obstacle reaches the screen edges
                Obstacle['direction'] *= -1  # Reverse the direction of the obstacle

            pygame.draw.rect(screen, BLACK, pygame.Rect(Obstacle['x'], Obstacle['y'], 50, 50))  # Draw the obstacle

            # Check for collision between Car1 and the obstacle (Had to check Stack Overflow for the math behind it)
            if (car1_x < Obstacle['x'] + 50 and car1_x + 100 > Obstacle['x'] and
                    car1_y < Obstacle['y'] + 50 and car1_y + 40 > Obstacle['y']):
                car1_x, car1_y = 100, 200  # Reset Car1 position

            # Check for collision between Car2 and the obstacle (Had to check Stack Overflow for the math behind it)
            if (car2_x < Obstacle['x'] + 50 and car2_x + 100 > Obstacle['x'] and
                    car2_y < Obstacle['y'] + 50 and car2_y + 40 > Obstacle['y']):
                car2_x, car2_y = 100, 300  # Reset Car2 position 

        # Show the cars on the screen
        screen.blit(car1_img, (car1_x, car1_y))
        screen.blit(car2_img, (car2_x, car2_y))

        # Check if Car1 reaches the end of the screen
        if car1_x >= screen_width:
            winner = "Player One"  # Set the winner to Player One
            winner_start_time = time.time()  # Record the time when the player wins
            game_state = "winner"  # Change the game state to "winner"
        elif car2_x >= screen_width:
            winner = "Player Two"  # Set the winner to Player Two
            winner_start_time = time.time()  # Record the time when the player wins
            game_state = "winner"  # Change the game state to "winner"
        # I had to record the time so the computer has to wait or else it would immediatley go to the winner game state

    elif game_state == "winner":  # If the game state is "winner"
        elapsed_time = time.time() - winner_start_time  # Calculate the elapsed time since the win

        font = pygame.font.SysFont(None, 48)  # Create a font object
        # Render the winner text
        winner_display = font.render(f"{winner} wins!", True, BLACK)
        # Display the winner text at the center of the screen
        screen.blit(winner_display, (screen_width // 2 - winner_display.get_width() // 2, screen_height // 2 - winner_display.get_height() // 2))
        pygame.display.flip()  # Update the display

        if elapsed_time >= 3:  # If 3 seconds have passed since the win
            game_state = "start"  # Reset the game state to "start"
            winner = None  # Clear the winner

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit pygame
