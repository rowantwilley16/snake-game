# snake-game
 
This is a simple Snake Game implemented in Python using the Pygame library.

## Description

The Snake Game is a classic arcade game where the player controls a snake that moves around the screen, eating food pellets to grow longer. The game ends if the snake collides with itself, the screen borders, or obstacles.

## Features

- Classic Snake gameplay
- Randomly generated obstacles
- Score tracking
- Game over screen
- Main menu with start button

## Implementation using linked lists 

1. **Snake Body Representation**:
   - In the Snake Game, the snake is represented as a series of connected segments forming its body.
   - Each segment of the snake's body is stored as a node in a linked list.
   - The linked list allows for efficient insertion of new segments at the head and removal of segments from the tail.

2. **Linked List Implementation**:
   - The linked list used for representing the snake's body is implemented with nodes.
   - Each node contains the coordinates of a segment (x, y) and a reference to the next node in the list.
   - The head of the linked list represents the front of the snake, and subsequent nodes represent the rest of the body.

3. **Moving the Snake**:
   - To move the snake, the game updates the coordinates of the head of the linked list based on the direction input from the player.
   - After moving the head, the game inserts a new node at the head's new position and removes the tail node, effectively simulating the snake's movement.

4. **Eating Fruit**:
   - When the snake eats a piece of fruit, the game adds a new segment to the snake's body without removing the tail node.
   - This allows the snake to grow longer while maintaining its previous length.

5. **Collision Detection**:
   - Collision detection is performed by checking whether the snake's head collides with its body segments, the screen borders, or obstacles.
   - If a collision occurs, the game ends, and the player is presented with a game over screen.

6. **Obstacles**:
   - Obstacles are represented as coordinates stored separately from the snake's body.
   - Collision detection with obstacles is performed similarly to collision detection with the snake's body segments.

## How to Play

1. Clone the repository: git clone https://github.com/rowantwilley16/snake_game.git

2. Install the required dependencies: pip install pygame pygame_gui

3. Run the game: python snake_game.py

4. Use the arrow keys to control the snake and eat the fruit. Avoid colliding with the snake itself, screen borders, and obstacles.

5. After game over, you will be taken back to the main menu.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).








