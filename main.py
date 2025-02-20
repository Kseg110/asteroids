# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
	pygame.init() #initializing pygame
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set GUI window/ format size
	print( "Starting asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")

# time clock object 
	clock = pygame.time.Clock() # created time clock object 
	dt = 0 

#game loop start 
	BLACK = (0, 0, 0) #set color variable to black for while loop
	while True:
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

#fill screen
		screen.fill(BLACK, rect=None, special_flags=0) 

# Update display 
		pygame.display.flip()

# time that has passed
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
