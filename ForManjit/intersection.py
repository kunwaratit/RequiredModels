import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
ROAD_WIDTH = 100
CAR_RADIUS = 10
CAR_SPEED = 5
MAX_LEFT_LANE_CARS = 5
MAX_RIGHT_LANE_CARS = 5
MAX_TOP_LANE_CARS = 5
MAX_BOTTOM_LANE_CARS = 5
CAR_DELAY = 100
GREEN_STATE = 0
YELLOW_STATE = 1
RED_STATE = 2
FPS = 60
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
def check_min_distance(new_car, existing_cars):
    min_distance = CAR_RADIUS * 4  # Minimum distance of half the radius

    for car in existing_cars:
        distance = ((new_car[0] - car[0]) ** 2 + (new_car[1] - car[1]) ** 2) ** 0.5
        if distance < min_distance:
            return False
    return True

def spawn_car(lane_cars, spawn_position):
    new_car = spawn_position
    while not check_min_distance(new_car, lane_cars):
        # Adjust x or y coordinate until the minimum distance is satisfied
        new_car[0] += random.choice([-1, 1]) * CAR_SPEED
        new_car[1] += random.choice([-1, 1]) * CAR_SPEED

    lane_cars.append(new_car)
def update_game_logic(left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars,
                       left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter,
                       traffic_light_state):
    def check_min_distance(new_car, existing_cars):
        min_distance = CAR_RADIUS * 4  # Minimum distance of half the radius

        for car in existing_cars:
            distance = ((new_car[0] - car[0]) ** 2 + (new_car[1] - car[1]) ** 2) ** 0.5
            if distance < min_distance:
                return False
        return True


    # Update positions of left lane cars
    for car in left_lane_cars:
        car[0] += CAR_SPEED
        car[1] = HEIGHT // 2 - ROAD_WIDTH // 4 - CAR_RADIUS // 2  # Adjust y-coordinate to stay inside the road

    # Update positions of right lane cars
    for car in right_lane_cars:
        car[0] -= CAR_SPEED  # Move horizontally
        car[1] = HEIGHT // 2 + ROAD_WIDTH // 4 - CAR_RADIUS // 2  # Adjust y-coordinate to stay inside the road

    # Update positions of top lane cars
    for car in top_lane_cars:
        car[1] += CAR_SPEED
        car[0] = WIDTH // 2 + ROAD_WIDTH // 4 - CAR_RADIUS // 2

    # Update positions of bottom lane cars
    for car in bottom_lane_cars:
        car[1] -= CAR_SPEED
        car[0] = WIDTH // 2 - ROAD_WIDTH // 4 - CAR_RADIUS // 2

    # Remove cars that have moved out of the screen width or height
    left_lane_cars[:] = [car for car in left_lane_cars if car[0] < WIDTH]
    right_lane_cars[:] = [car for car in right_lane_cars if car[0] > 0 and car[1] > 0]
    top_lane_cars[:] = [car for car in top_lane_cars if car[1] < HEIGHT]
    bottom_lane_cars[:] = [car for car in bottom_lane_cars if car[1] > 0]

    # Count the number of cars entering the left lane
    if random.random() < 0.02 and len(left_lane_cars) < MAX_LEFT_LANE_CARS:
        spawn_car(left_lane_cars, [0, HEIGHT // 2 - ROAD_WIDTH // 4 - CAR_RADIUS // 2])

    # Spawn cars in right lane
    if random.random() < 0.02 and len(right_lane_cars) < MAX_RIGHT_LANE_CARS:
        spawn_car(right_lane_cars, [WIDTH, HEIGHT // 2 + ROAD_WIDTH // 4 - CAR_RADIUS // 2])

    # Spawn cars in top lane
    if random.random() < 0.02 and len(top_lane_cars) < MAX_TOP_LANE_CARS:
        spawn_car(top_lane_cars, [WIDTH // 2 + ROAD_WIDTH // 4 - CAR_RADIUS // 2, 0])

    # Spawn cars in bottom lane
    if random.random() < 0.02 and len(bottom_lane_cars) < MAX_BOTTOM_LANE_CARS:
        spawn_car(bottom_lane_cars, [WIDTH // 2 - ROAD_WIDTH // 4 - CAR_RADIUS // 2, HEIGHT])

    return left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter

def draw_on_screen(left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars, left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter, traffic_light_timer):
    screen.fill(BROWN)

    # Draw roads
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2 - ROAD_WIDTH // 2, WIDTH, ROAD_WIDTH))  # Bottom road
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, HEIGHT))  # Right road

    # Draw white lines to split the roads
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 4)  # Split bottom road
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 4)  # Split right road

    # Draw intersections
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, ROAD_WIDTH))  # Top
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - ROAD_WIDTH // 2, HEIGHT - ROAD_WIDTH, ROAD_WIDTH, ROAD_WIDTH))  # Bottom
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2 - ROAD_WIDTH // 2, ROAD_WIDTH, ROAD_WIDTH))  # Left
    pygame.draw.rect(screen, GRAY, (WIDTH - ROAD_WIDTH, HEIGHT // 2 - ROAD_WIDTH // 2, ROAD_WIDTH, ROAD_WIDTH))  # Right

    # Draw lines before every intersection with traffic light logic
    if traffic_light_state == GREEN_STATE:
        pygame.draw.line(screen, GREEN, (WIDTH // 2 - ROAD_WIDTH // 2 - 10, 250), (WIDTH // 2 - ROAD_WIDTH // 2 - 10, HEIGHT - 300), 5)  # Left intersection line
        pygame.draw.line(screen, GREEN, (WIDTH // 2 + ROAD_WIDTH // 2 + 10, 300), (WIDTH // 2 + ROAD_WIDTH // 2 + 10, HEIGHT - 250), 5)  # Right intersection line
        pygame.draw.line(screen, RED, (400, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), (450, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), 5)  # Top intersection line
        pygame.draw.line(screen, RED, (350, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), (400, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), 5)  # Bottom intersection line
    elif traffic_light_state == YELLOW_STATE:
        pygame.draw.line(screen, YELLOW, (WIDTH // 2 - ROAD_WIDTH // 2 - 10, 250), (WIDTH // 2 - ROAD_WIDTH // 2 - 10, HEIGHT - 300), 5)  # Left intersection line
        pygame.draw.line(screen, YELLOW, (WIDTH // 2 + ROAD_WIDTH // 2 + 10, 300), (WIDTH // 2 + ROAD_WIDTH // 2 + 10, HEIGHT - 250), 5)  # Right intersection line
        pygame.draw.line(screen, YELLOW, (400, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), (450, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), 5)  # Top intersection line
        pygame.draw.line(screen, YELLOW, (350, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), (400, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), 5)  # Bottom intersection line
    elif traffic_light_state == RED_STATE:
        pygame.draw.line(screen, RED, (WIDTH // 2 - ROAD_WIDTH // 2 - 10, 250), (WIDTH // 2 - ROAD_WIDTH // 2 - 10, HEIGHT - 300), 5)  # Left intersection line
        pygame.draw.line(screen, RED, (WIDTH // 2 + ROAD_WIDTH // 2 + 10, 300), (WIDTH // 2 + ROAD_WIDTH // 2 + 10, HEIGHT - 250), 5)  # Right intersection line
        pygame.draw.line(screen, GREEN, (400, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), (450, HEIGHT // 2 - ROAD_WIDTH // 2 - 10), 5)  # Top intersection line
        pygame.draw.line(screen, GREEN, (350, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), (400, HEIGHT // 2 + ROAD_WIDTH // 2 + 10), 5)  # Bottom intersection line

    # Draw left lane cars
    for car in left_lane_cars:
        pygame.draw.circle(screen, RED, (int(car[0]), int(car[1])), CAR_RADIUS)

    # Draw right lane cars
    for car in right_lane_cars:
        pygame.draw.circle(screen, WHITE, (int(car[0]), int(car[1])), CAR_RADIUS)

    # Draw top lane cars
    for car in top_lane_cars:
        pygame.draw.circle(screen, RED, (int(car[0]), int(car[1])), CAR_RADIUS)

    # Draw bottom lane cars
    for car in bottom_lane_cars:
        pygame.draw.circle(screen, WHITE, (int(car[0]), int(car[1])), CAR_RADIUS)

    # Display left lane car count
    font = pygame.font.Font(None, 36)
    text = font.render(f"Left Lane Cars: {left_lane_counter}", True, WHITE)
    screen.blit(text, (10, 360))

    # Display top lane car count
    text = font.render(f"Top Lane Cars: {top_lane_counter}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 100, 20))

    # Display right lane car count
    text = font.render(f"Right Lane Cars: {right_lane_counter}", True, WHITE)
    screen.blit(text, (WIDTH - 250, HEIGHT // 2 + 50))

    # Display bottom lane car count
    text = font.render(f"Bottom Lane Cars: {bottom_lane_counter}", True, WHITE)
    screen.blit(text, (WIDTH - 480, 560))

    pygame.display.flip()  # Update the display

# Main game loop
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulator")

clock = pygame.time.Clock()

left_lane_cars = []
right_lane_cars = []
top_lane_cars = []
bottom_lane_cars = []

left_lane_counter = 0
top_lane_counter = 0
right_lane_counter = 0
bottom_lane_counter = 0

traffic_light_state = GREEN_STATE
traffic_light_timer = 0
running = True

while running:
    clock.tick(FPS)

    running = handle_events()

    traffic_light_timer = (traffic_light_timer + 1) % (FPS * 25)  # 25 seconds cycle (green: 10s, yellow: 5s, red: 10s)

    if 0 <= traffic_light_timer < 10 * FPS:
        traffic_light_state = GREEN_STATE
    elif 10 * FPS <= traffic_light_timer < 15 * FPS:
        traffic_light_state = YELLOW_STATE
    elif 15 * FPS <= traffic_light_timer < 25 * FPS:
        traffic_light_state = RED_STATE

    left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter = update_game_logic(
        left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars,
        left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter, traffic_light_state
    )

    draw_on_screen(left_lane_cars, right_lane_cars, top_lane_cars, bottom_lane_cars,
                   left_lane_counter, top_lane_counter, right_lane_counter, bottom_lane_counter,
                   traffic_light_timer)

pygame.quit()
