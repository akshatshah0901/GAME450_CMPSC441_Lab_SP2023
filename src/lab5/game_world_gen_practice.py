'''
Lab 5: PCG and Project Lab
This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes


# TODO: Demo blittable surface helper function

''' Create helper functions here '''

if __name__ == "__main__":
    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3]) 

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    city_locations = [] 
    routes = []

    ''' Setup cities and routes in here'''

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10] 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))
        routes = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('J', 'K'), ('K', 'L')]
        city_locations_dict = {'A': (100,105),
                       'B': (400, 100) ,
                        'C': (320,40),
                       'D': (230,300),
                       'E': (126,283),'F':
                           (80,400),'G': (200,600),
                       'H': (100,567),'I': (400,600), 'J': (115,300), 'K': (400,400), 'L': (250,250)}


      
        ''' draw cities '''
        city_dimensions = 5
        city_color = (0, 0, 255)
        for city_location in city_locations:
             city_surface = pygame.Surface((city_dimensions*2, city_dimensions*2))
             city_surface.fill(city_color)
             pygame.draw.circle(city_surface, (255, 255, 255), (city_dimensions, city_dimensions), city_dimensions, 0)
             screen.blit(city_surface, (city_location[0]-city_dimensions, city_location[1]-city_dimensions))

        ''' draw first 10 routes '''
        for route in routes:
            start, end = route
            start_x, start_y = city_locations_dict[start]
            end_x, end_y = city_locations_dict[end]
            pygame.draw.line(screen, (0, 0, 255), (start_x, start_y), (end_x, end_y), 2)  
    
            pygame.display.flip()
