# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import *

print( "Starting asteroids!")
print("Screen width: 1280")
print("Screen height: 720")

def main():
	pygame.init() #initializing pygame
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set GUI window/ format size
# time clock object 
	clock = pygame.time.Clock() # created time clock object 
	dt = 0 

# Creating groupds for updatables & Drawables using pygames groups/containers 
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
# create player instance 
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
#game loop start 
	BLACK = (0, 0, 0) #set color variable to black for while loop
	while True:
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt) # applied update method to update player object for each frame before rendering
		screen.fill(BLACK, rect=None, special_flags=0) #fill screen
		for obj in drawable:
			obj.draw(screen)# draw the player here
		pygame.display.flip()# Update display
		
# CAPTURE DELTA time that has passed
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
