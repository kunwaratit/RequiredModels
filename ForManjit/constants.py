# constants.py
import pygame

# Define colors
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
BROWN = (218, 160, 109)
GREEN = (0,255,0)
YELLOW=(255, 255, 0)
# Define road properties
ROAD_WIDTH = 100
CAR_RADIUS = 8
CAR_SPEED = 5
MAX_LEFT_LANE_CARS = 5
MAX_RIGHT_LANE_CARS = 10
MAX_TOP_LANE_CARS = 5
MAX_BOTTOM_LANE_CARS = 10
CAR_DELAY = 30

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersection Simulation")

# Initialize clock outside the main loop
clock = pygame.time.Clock()
FPS = 30 