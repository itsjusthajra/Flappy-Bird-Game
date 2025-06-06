import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 554
screen_height = 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Clock and FPS
clock = pygame.time.Clock()
fps = 60

# Fonts & Colors
font = pygame.font.SysFont('Bauhaus 93', 60)
button_font = pygame.font.SysFont('Bauhaus 93', 40)
white = (255, 255, 255)

# Ground settings
ground_width = 554
ground_height = 65
ground_y = screen_height - ground_height
groundmove = 0
movespeed = 4
pipegap = 400
pipe_frequency = 1500  # milliseconds
score = 0
passpipe = False

# Game states
flying = False  
gameover = False  

# Load images
background = pygame.image.load("background.png")
ground = pygame.image.load("ground.png")

def draw_text(text, font, text_col, y):
    """Center and draw text on the screen."""
    img = font.render(text, True, text_col)
    x = (screen_width - img.get_width()) // 2
    screen.blit(img, (x, y))

def draw_button(text, x, y, width, height, color, action=None):
    """Draws a button and handles clicks."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button Rect
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)

    # Draw button text
    text_img = button_font.render(text, True, white)
    text_x = x + (width - text_img.get_width()) // 2
    text_y = y + (height - text_img.get_height()) // 2
    screen.blit(text_img, (text_x, text_y))

    # Button click detection
    if button_rect.collidepoint(mouse) and click[0] == 1:
        if action:
            action()

def restart_game():
    """Resets all game variables to restart."""
    global flying, gameover, score, passpipe, pipe_group, flappy, last_pipe
    flying = False
    gameover = False
    score = 0
    passpipe = False
    pipe_group.empty()
    flappy.rect.center = (50, screen_height // 2)
    flappy.vel = 0
    last_pipe = pygame.time.get_ticks() - pipe_frequency  # Reset pipe spawn timer

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(f'Bird{num}.png') for num in range(1, 4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.vel = 0  
        self.clicked = False  

    def update(self):
        if flying or gameover:
            if flying:
                self.vel = min(self.vel + 0.5, 8)
                if self.rect.bottom < ground_y:
                    self.rect.y += int(self.vel)

        if not gameover:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            if self.counter > 5:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images)

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -135)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipegap // 2)
        else:
            self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= movespeed
        if self.rect.right < 0:
            self.kill()

# Create bird and add to sprite group
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(50, screen_height // 2)
bird_group.add(flappy)

# Track the last time pipes were spawned
last_pipe = pygame.time.get_ticks() - pipe_frequency

# Main game loop
run = True
while run:
    clock.tick(fps)
    screen.blit(background, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)

    screen.blit(ground, (groundmove, ground_y))
    screen.blit(ground, (groundmove + ground_width, ground_y))
    if len(pipe_group) > 0:
        first_pipe = pipe_group.sprites()[0]
        if flappy.rect.left > first_pipe.rect.right and not passpipe:
            score += 1
            passpipe = True
        if flappy.rect.left < first_pipe.rect.left:
            passpipe = False

    draw_text(str(score), font, white, 20)

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        gameover = True

    if flappy.rect.bottom >= ground_y:
        gameover = True
        flying = False

    if not gameover and flying:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            pipe_group.add(Pipe(screen_width, screen_height // 2 + pipe_height, -1))
            pipe_group.add(Pipe(screen_width, screen_height // 2 + pipe_height, 1))
            last_pipe = time_now  # Update the last pipe spawn time
        groundmove -= movespeed
        if groundmove <= -ground_width:
            groundmove = 0
        pipe_group.update()
       
    # **Game Over Screen**
    if gameover:
        draw_text("GAME OVER", font, white, 200)
        draw_button("Restart", 180, 300, 200, 50, (0, 170, 0), restart_game)
        draw_button("Quit", 180, 370, 200, 50, (170, 0, 0), pygame.quit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not gameover:
            flying = True
        if event.type == pygame.KEYDOWN and not gameover:
            if event.key == pygame.K_SPACE:
                flappy.vel = -10  # Make the bird flap

    pygame.display.update()

pygame.quit()