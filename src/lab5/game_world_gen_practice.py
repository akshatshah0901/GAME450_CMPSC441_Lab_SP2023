import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path

sys.path.append(str((Path(__file__) / '..' / '..').resolve().absolute()))
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
    routes = get_routes(city_names)

    ''' Setup cities and routes in here'''

    get_randomly_spread_cities()

    get_routes()

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        ''' draw cities '''
    pygame.draw.circle(size, get_randomly_spread_cities, 5)
    Hello
    route_color = (0, 0, 255)
    ''' draw first 10 routes '''

routes = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('J', 'K'), ('K', 'L')]
city_locations_dict = {'A': (12,342),
                       'B': (20, 400) ,
                        'C': (30,40),
                       'D': (50,70),
                       'E': (16,283),'F':
                           (40,605),'G': (13,222),
                       'H': (43,567),'I': (19,332), 'J': (24,200), 'K': (32,453), 'L': (21,2321)}


print(city_locations_dict['A'])
pygame.display.flip()
