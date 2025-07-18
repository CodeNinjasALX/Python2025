import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Super Mario")

# Load assets
mario_img = pygame.image.load('mario.png') # Replace with your Mario image path
background_img = pygame.image.load('background.png') # Replace with your background image path

# Mario properties
mario_x, mario_y = 50, 300
mario_speed = 5

# Game loop
running = True
while running:
screen.fill("WHITE")
screen.blit(background_img, (0, 0)) # Draw background
screen.blit(mario_img, (mario_x, mario_y)) # Draw Mario

for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

# Controls for Mario movement
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
mario_x -= mario_speed
if keys[pygame.K_RIGHT]:
mario_x += mario_speed
if keys[pygame.K_UP]:
mario_y -= mario_speed
if keys[pygame.K_DOWN]:
mario_y += mario_speed

# Update display
pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()