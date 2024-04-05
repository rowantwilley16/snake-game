import pygame,pygame_gui
import time
import random
from pygame.locals import *
from pygame_gui import UIManager, elements

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Window size
window_x = 720
window_y = 480
block_size = 10

# Snake speed
snake_speed = 15

# Snake direction
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            pop_data = self.head.data
            self.head = None
            return pop_data
        else:
            current = self.head
            while current.next.next:
                current = current.next
            pop_data = current.next.data
            current.next = None
            return pop_data

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Function to generate random obstacles
def generate_obstacles():
    obstacles = []
    for _ in range(20):  # Generate 20 obstacles
        obstacle_x = random.randrange(0, window_x, block_size)
        obstacle_y = random.randrange(0, window_y, block_size)
        obstacles.append([obstacle_x, obstacle_y])
    return obstacles
# Main game function
def game_loop():
    # Initialise pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # Define snake position
    snake_position = [100, 50]

    # Define snake body
    snake_body = LinkedList()
    snake_body.append([100, 50])
    snake_body.append([90, 50])
    snake_body.append([80, 50])
    snake_body.append([70, 50])

    # Define fruit position
    fruit_position = [random.randrange(1, (window_x // block_size)) * block_size,
                      random.randrange(1, (window_y // block_size)) * block_size]
    fruit_spawn = True

    # Define obstacles
    obstacles = generate_obstacles()

    # Set default snake direction
    direction = RIGHT
    change_to = direction

    # Initial score
    score = 0

    # Function to display score
    def show_score():
        font = pygame.font.SysFont('times new roman', 20)
        score_surface = font.render('Score: ' + str(score), True, white)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (window_x // 2, 10)
        game_window.blit(score_surface, score_rect)

    # Game over function
    def game_over():
        font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = font.render('Game Over', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x // 2, window_y // 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
    
        # Wait for 5 seconds
        start_time = time.time()
        while time.time() - start_time < 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # Return to main menu
        main_menu(window)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Handling key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = UP
                if event.key == pygame.K_DOWN:
                    change_to = DOWN
                if event.key == pygame.K_LEFT:
                    change_to = LEFT
                if event.key == pygame.K_RIGHT:
                    change_to = RIGHT

        # Set snake direction based on user input
        if change_to == UP and direction != DOWN:
            direction = UP
        if change_to == DOWN and direction != UP:
            direction = DOWN
        if change_to == LEFT and direction != RIGHT:
            direction = LEFT
        if change_to == RIGHT and direction != LEFT:
            direction = RIGHT

        # Move snake
        if direction == UP:
            snake_position[1] -= block_size
        if direction == DOWN:
            snake_position[1] += block_size
        if direction == LEFT:
            snake_position[0] -= block_size
        if direction == RIGHT:
            snake_position[0] += block_size

        # Check if snake collides with screen borders
        if (snake_position[0] < 0 or snake_position[0] >= window_x or
            snake_position[1] < 0 or snake_position[1] >= window_y):
            game_over()

        # Insert new head into snake body
        snake_body.insert(list(snake_position))

        # Check if snake collides with obstacles
        for obstacle in obstacles:
            if snake_position == obstacle:
                game_over()

        # Check if snake eats fruit
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        # Respawn fruit
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // block_size)) * block_size,
                              random.randrange(1, (window_y // block_size)) * block_size]
            fruit_spawn = True

        # Draw game window
        game_window.fill(black)

        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(game_window, blue, pygame.Rect(obstacle[0], obstacle[1], block_size, block_size))

        # Draw snake
        current = snake_body.head
        while current:
            pygame.draw.rect(game_window, green, pygame.Rect(current.data[0], current.data[1], block_size, block_size))
            current = current.next

        # Draw fruit
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], block_size, block_size))

        # Display score
        show_score()

        # Update display
        pygame.display.update()

        # Control snake speed
        fps.tick(snake_speed)
# Main menu function
def main_menu(screen):
    manager = UIManager((window_x, window_y))
    start_button = elements.UIButton(relative_rect=pygame.Rect((window_x // 2 - 50, window_y // 2 - 25), (100, 50)),
                                     text='Start', manager=manager)
    
    running = True
    while running:
        time_delta = pygame.time.Clock().tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        running = False
                        # Manually remove UI elements
                        start_button.kill()
                        manager.clear_and_reset()
                        game_loop()
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill(black)
        manager.draw_ui(screen)
        pygame.display.update()

# Main function
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('Snake Game')
    main_menu(window)
