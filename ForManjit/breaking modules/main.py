# main.py
import pygame
import sys
from intersection import handle_events, update_game_logic, draw_on_screen

from constants import WIDTH, HEIGHT, clock, FPS

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersection Simulation")
red_lines_state = {'horizontal_crossed': False, 'vertical_crossed': False}
# Initialize left and right lane cars, top and bottom lane cars
left_lane_cars = []
right_lane_cars = []
top_lane_cars = []
bottom_lane_cars = []

# Initialize left lane, top lane, right lane, and bottom lane counters
left_lane_counter = 0
top_lane_counter = 0
right_lane_counter = 0
bottom_lane_counter = 0
# Main game loop

# Main game loop
running = True
traffic_light_timer = 0
red_lines_state = {'horizontal_crossed': False, 'vertical_crossed': False}

while running:
    clock.tick(30)  # Set the frame rate

    running = handle_events()

    # Update traffic light timer
    traffic_light_timer = (traffic_light_timer + 1) % (FPS * 20)  # 20 seconds cycle (green: 10s, red: 10s)

    # Update game logic based on traffic light timer
    left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter = update_game_logic(
        left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars,
        left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter,
        traffic_light_timer, red_lines_state  # Make sure to include red_lines_state
    )

    # Check if cars have crossed the red lines
    red_lines_state['horizontal_crossed'] = any(car[0] > 350 and car[0] < 450 for car in left_lane_cars + right_lane_cars)
    red_lines_state['vertical_crossed'] = any(car[1] > 250 and car[1] < 350 for car in top_lane_cars + bottom_lane_cars)

    # Draw the scene
    draw_on_screen(left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars,
                   left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter,
                   traffic_light_timer, is_orange_light_on, red_lines_state['horizontal_crossed'], red_lines_state['vertical_crossed']) 

pygame.quit()
sys.exit()