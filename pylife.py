"""
Rules:

Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import os
import time

# Setup

width = 20
height = 20
world = """                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    XXXXX           
    XXXXX           
                    
                    
                    
                    
                    
                    """


newworld = []

world = world.split("\n")
for i in range(len(world)):
	world[i] = list(world[i])

newworld = world
print(world)

# Test

def test(x,y):
	neighbours = 0
	is_live = False

	if world[x][y] == "X":
		is_live = True

	if world[x-1][y] == "X":
		neighbours += 1
	if world[x+1][y] == "X":
		neighbours += 1
	if world[x-1][y-1] == "X":
		neighbours += 1
	if world[x][y-1] == "X":
		neighbours += 1
	if world[x+1][y-1] == "X":
		neighbours += 1
	if world[x-1][y+1] == "X":
		neighbours += 1
	if world[x][y+1] == "X":
		neighbours += 1
	if world[x+1][y+1] == "X":
		neighbours += 1

	if is_live:
		if neighbours < 2:
			return " "
		if neighbours == 2 or neighbours == 3:
			return "X"
		if neighbours > 3:
			return " "
	else:
		if neighbours == 3:
			return "X"
		else:
			return " "

# Render

def render(world):
	os.system('clear')
	world = newworld
	for i in range(len(newworld)):
		line = "".join(newworld[i])
		print(line)

render(world)

# Main loop

def main():
	while True:
		for y in range(1,height-1):
			for x in range(1,width-1):
				newworld[x][y] = test(x,y)
		render(newworld)
		time.sleep(0.1)

main()