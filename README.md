# Flappy-Bird-Game
## Overview
This project is a Python implementation of the classic Flappy Bird game using the Pygame library. The game features a bird that navigates through a series of pipes by flapping its wings, with the goal of achieving the highest score possible. The game includes a start screen, a game-over screen with restart and quit buttons, and a scoring system. The bird's animation, pipe generation, and collision detection are all handled dynamically.

## Features
- **Bird Animation**: The bird flaps its wings using a sprite animation with three frames (Bird1.png, Bird2.png, Bird3.png).
- **Dynamic Pipe Generation**: Pipes are generated at random heights with a fixed gap for the bird to pass through.
- **Scoring System**: The player earns a point each time the bird passes through a pair of pipes.
- **Game States**: Includes start, flying, and game-over states with appropriate UI elements.
- **Interactive Controls**: Use mouse clicks or the spacebar to make the bird flap.
- **Restart and Quit Options**: Buttons on the game-over screen allow the player to restart or quit the game.
## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Pygame Library**: The game requires the Pygame library to run. Install it using: ```bash pip install pygame ```
## Files
- **Game.py**: The main game script containing all the game logic.
- **background.png**: The background image for the game.
- **ground.png**: The scrolling ground image (dimensions: 554x65 pixels).
- **pipe.png**: The pipe image used for obstacles.
- **Bird1.png, Bird2.png, Bird3.png**: Three images for the bird's animation frames.
## File Requirements
- Ensure all image files (background.png, ground.png, pipe.png, Bird1.png, Bird2.png, Bird3.png) are in the same directory as Game.py.
- The ground image must have dimensions of 554x65 pixels to match the ground_width and ground_height variables.
- The background image should match the screen dimensions (554x600 pixels) for proper rendering.
## How to Run
- **Set Up the Environment**:
  - Install Python 3.x if not already installed.
  - Install Pygame using the command above.
  - Place all required image files in the same directory as Game.py.
- **Run the Game**:
    - Open a terminal or command prompt in the project directory.
    - **Execute the following command**: ```bash python Game.py ```
- **Gameplay**:
   - Click the mouse or press the spacebar to start the game.
   - Use mouse clicks or the spacebar to make the bird flap and navigate through the pipes.
   - Avoid hitting the pipes, the ground, or the top of the screen.
   - When the game is over, use the "Restart" button to play again or the "Quit" button to exit.
## Game Mechanics
### Controls
- **Start the Game**: Click the mouse or press the spacebar to begin flying.
- **Flap the Bird**: Click the mouse or press the spacebar to make the bird flap its wings, causing it to rise.
- **Restart**: On the game-over screen, click the "Restart" button to play again.
- **Quit**: On the game-over screen, click the "Quit" button to exit the game.
### Scoring
- The score is displayed at the top center of the screen.
- You earn 1 point each time the bird passes through a pair of pipes.
- The score resets to 0 when the game restarts.
### Game Over Conditions
- **The game ends if the bird**:
   - Collides with a pipe.
   - Hits the ground (y-position >= 535).
   - Hits the top of the screen (y-position <= 0).
When the game ends, the bird rotates to a downward angle (-135 degrees) to simulate falling.
## Customization
### Screen and Ground Settings
- **Screen Dimensions**: The screen size is set to 554x600 pixels (screen_width, screen_height). Adjust these values in the code to change the window size, but ensure the background image matches the new dimensions.
- **Ground Settings**:
ground_width and ground_height are set to 554 and 65 pixels, respectively, to match the ground image.
ground_y is calculated as screen_height -  ground_height (535 pixels).
The ground scrolls left at a speed of movespeed (4 pixels per frame). Adjust movespeed to change the scrolling speed.
### Pipe Settings
- **Pipe Gap**: The gap between the top and bottom pipes is set by pipegap (400 pixels). Adjust this value to make the game easier or harder.
- **Pipe Frequency**: New pipes spawn every pipe_frequency milliseconds (1500 ms). Modify this to change how often pipes appear.
- **Pipe Height Variation**: The pipe height varies randomly by random.randint(- 100, 100). Adjust the range to change the difficulty.
### Bird Settings
- **Starting Position**: The bird starts at (50, screen_height // 2) (50, 300). Modify this in the Bird class or restart_game function to change the starting position.
- **Flap Strength**: The bird's upward velocity when flapping is set to - 10 (self.vel = -10). Adjust this to change how high the bird jumps.
- **Gravity**: Gravity is simulated by increasing the velocity by 0.5 each frame (self.vel + 0.5), capped at 8. Modify these values to adjust the falling speed.
### Visuals
- **Fonts**: The game uses the "Bauhaus 93" font with sizes 60 for the score and game-over text, and 40 for buttons. Change the font or size by modifying the font and button_font variables.
- **Colors**: The text and button colors use white (255, 255, 255). Button colors are green (0, 170, 0) for "Restart" and red (170, 0, 0) for "Quit". Adjust these in the code as needed.
## Code Structure
### Main Classes
- **Bird Class**:
Manages the bird sprite, animation, and movement.
Uses three images (Bird1.png, Bird2.png, Bird3.png) for animation, cycling every 5 frames.
Handles gravity, flapping, and rotation based on velocity.
- **Pipe Class**:
Manages pipe sprites, positioning them as top or bottom pipes.
Pipes move left at movespeed and are removed when off- screen.
### Helper Functions
- **draw_text**: Centers and draws text on the screen (used for score and game-over text).
- **draw_button**: Draws interactive buttons for the game-over screen (Restart and Quit).
- **restart_game**: Resets all game variables to restart the game.
### Game Loop
Runs at 60 FPS (fps).
Handles event processing, updates sprites, checks collisions, and renders the game.
Manages game states (flying, gameover) to control gameplay flow.
## Troubleshooting
- **Missing Images**: Ensure all image files are in the same directory as Game.py. If an image is missing, the game will crash with a FileNotFoundError.
- **Screen Size Mismatch**: If the background or ground images don’t match the screen dimensions, the visuals may look distorted. Adjust the dimensions in the code or resize the images.
- **Performance Issues**: If the game runs slowly, reduce the fps value or optimize the images (e.g., reduce their resolution).
## Future Improvements
- Add sound effects for flapping, scoring, and collisions.
- Implement a high- score system that persists across sessions.
- Add more bird animations or skins for variety.
- Introduce difficulty levels by adjusting pipe gap and frequency dynamically.
## Notes
- The game assumes the system has the "Bauhaus 93" font installed. If unavailable, Pygame will use a default font, which may affect the appearance.
- The pipe image (pipe.png) is flipped vertically for the top pipe. Ensure the image is designed to look correct when flipped.
- The game loop runs at 60 FPS, which should be smooth on most systems, but performance may vary depending on hardware.
