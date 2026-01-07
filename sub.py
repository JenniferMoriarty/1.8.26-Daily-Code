# Submarine Static Picture - Fix-the-Numbers Activity (EASIER)
#
# Student goal:
# - It RUNS, but a few things are wrong on purpose.
# - Keep the submarine mostly correct and fix: sand, bubbles, periscope, and 2 windows.
# - You may ONLY change numbers (colors, positions, sizes, counts).
#
# Mouse (x, y) prints to the console to help you line things up.

import pygame
import sys
import random

pygame.init()

# Display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Submarine Static Picture")

# Colors (some correct, some wrong on purpose)
OCEAN_BLUE = (0, 75, 150)          # CORRECT
SUB_YELLOW = (255, 215, 0)         # CORRECT
SUB_DARK_YELLOW = (200, 170, 0)    # CORRECT

WINDOW_CYAN = (0, 255, 0)          # WRONG (should be cyan)
SAND_BEIGE = (178, 194, 128)       # WRONG (close-ish but wrong)
BUBBLE_WHITE = (255, 255, 255)     # WRONG (should be slightly bluish)

# Generate bubble positions once (a little wrong on purpose)
bubble_list = []
for i in range(25):  # WRONG (should be ~30)
    x = random.randrange(0, screen_width)
    y = random.randrange(0, 560)   # WRONG (should stay above sand)
    r = random.randrange(3, 9)     # WRONG (should be smaller range)
    bubble_list.append((x, y, r))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Print mouse coordinates (helps students position shapes)
    mx, my = pygame.mouse.get_pos()
    print(f"Mouse: ({mx}, {my})")

    # --- DRAWING ---
    screen.fill(OCEAN_BLUE)

    # Sand (WRONG EDGE / WRONG POSITION)
    # Hint: sand belongs at the bottom.
    pygame.draw.rect(screen, SAND_BEIGE, [0, 0, 800, 80])

    # Bubbles (outline thickness is wrong on purpose)
    for b in bubble_list:
        pygame.draw.circle(screen, BUBBLE_WHITE, (b[0], b[1]), b[2], 2)  # should be 1

    # Periscope (WRONG POSITION)
    # Hint: periscope should be attached to the top of the sub.
    pygame.draw.rect(screen, SUB_DARK_YELLOW, [520, 120, 10, 70])
    pygame.draw.rect(screen, SUB_DARK_YELLOW, [520, 120, 30, 10])

    # Submarine Hull (CORRECT)
    pygame.draw.ellipse(screen, SUB_YELLOW, [250, 250, 350, 180])

    # Propeller / tail (CORRECT)
    prop_points = [(250, 340), (200, 300), (200, 380)]
    pygame.draw.polygon(screen, SUB_DARK_YELLOW, prop_points)

    # Windows: keep ONE window correct, two are wrong on purpose
    # Correct window (middle one)
    pygame.draw.circle(screen, WINDOW_CYAN, (400, 340), 25)  # position correct, color wrong
    pygame.draw.circle(screen, SUB_DARK_YELLOW, (400, 340), 25, 3)

    # Wrong windows (students fix)
    pygame.draw.circle(screen, WINDOW_CYAN, (260, 300), 18)  # wrong
    pygame.draw.circle(screen, SUB_DARK_YELLOW, (260, 300), 18, 4)

    pygame.draw.circle(screen, WINDOW_CYAN, (520, 380), 18)  # wrong
    pygame.draw.circle(screen, SUB_DARK_YELLOW, (520, 380), 18, 4)

    pygame.display.flip()

pygame.quit()
sys.exit()

