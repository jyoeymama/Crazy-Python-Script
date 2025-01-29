import random
import time
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Settings
WIDTH = 80
HEIGHT = 40
GRAVITY = 1
EXPLOSION_CHANCE = 0.02
CHARS = [Fore.RED + char + Style.RESET_ALL for char in "!@#$%^&*()_+-=[]{}|;:,.<>?/\\`~"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid():
    return [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def draw_grid(grid):
    clear_screen()
    for row in grid:
        print(''.join(row))

def apply_gravity(grid):
    for x in range(WIDTH):
        for y in range(HEIGHT - 1, 0, -1):
            if grid[y][x] == ' ' and grid[y - 1][x] != ' ':
                grid[y][x] = grid[y - 1][x]
                grid[y - 1][x] = ' '

def add_random_characters(grid):
    for x in range(WIDTH):
        if random.random() < 0.1:
            grid[0][x] = random.choice(CHARS)

def create_explosion(grid, x, y):
    for dx in range(-5, 6):  # Bigger explosion radius
        for dy in range(-5, 6):
            if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT:
                if random.random() < 0.5:
                    grid[y + dy][x + dx] = random.choice(CHARS)

def apply_explosions(grid):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if grid[y][x] != ' ' and random.random() < EXPLOSION_CHANCE:
                create_explosion(grid, x, y)

def save_grid(grid, filename="crazy_art.txt"):
    with open(filename, "w") as file:
        for row in grid:
            file.write(''.join(row) + '\n')

def main():
    grid = create_grid()
    try:
        while True:
            add_random_characters(grid)
            apply_gravity(grid)
            apply_explosions(grid)
            draw_grid(grid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        # Save the final grid when the user stops the script
        save_grid(grid)
        print("\nArt saved to 'crazy_art.txt'!")

if __name__ == "__main__":
    main()