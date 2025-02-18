# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

pygame.get_init() #initializing pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set GUI window/ format size

color = (r,g,b)
while True:
	screen.fill(color, rect=None, special_flags=0) #infinite while loop to fill screen with solid black color

def main():
	print( "Starting asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")

if __name__ == "__main__":
    main()
