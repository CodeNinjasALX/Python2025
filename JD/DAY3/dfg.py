import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BLACK_HOLE_MASS = 10**30  # Mass of the black hole in kg
G = 6.67430 * 10**-11  # Gravitational constant
SPEED_OF_LIGHT = 299792458  # Speed of light in m/s
BLACK_HOLE_RADIUS = 50  # Radius of the event horizon (in pixels)
OBJECT_RADIUS = 5
