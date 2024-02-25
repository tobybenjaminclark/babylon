from tkinter import *
import numpy as np
import configparser
from src_terrain_generation.bblyn_generate_heightmap import generate_heightmap
from src_terrain_generation.bblyn_generate_forestmap import generate_forestmap
from src_terrain_generation.bblyn_generate_rockmap import generate_rockmap
from src_terrain_generation.bblyn_generate_mountain import generate_mountain
from src_terrain_generation.bblyn_generate_resourcemap import generate_resource_map

# Define color ranges
colour_ranges = [
    (0, 'cyan3'),
    (30, 'cyan2'),
    (60, 'aquamarine'),
    (90, 'NavajoWhite3'),
    (92, 'NavajoWhite2'),
    (100, '#8aad6f'),
    (110, '#779e59'),
    (140, '#669144'),
    (190, '#5b853a'),
    (256, '#667a57'),
    (285, '#777a57'),
    (335, '#706f55'),
    (385, '#59594d'),
    (435, '#57554f'),
]

class GameCanvas(Canvas):

    def __init__(self, *args, **kwargs) -> None:
        self.load_settings()
        super().__init__(width=self.width, height=self.height, bg="black", *args, **kwargs)

        self.render_map()

        self.update()

    def render_map(self) -> None:
        global colour_ranges
        # Set the resolution and tileability for the Perlin noise
        shape = (self.width, self.height)
        # Generate Perlin noise
        normalized_map = generate_heightmap((self.width, self.height))

        normalized_map = generate_mountain(normalized_map, 250)
        forest_map = generate_forestmap(normalized_map)
        rockmap = generate_rockmap(normalized_map)
        resources = generate_resource_map(normalized_map, forest_map, rockmap)


        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Use the Perlin noise values to determine the color
                color_value = int(normalized_map[x, y])

                # Set default color
                fill_colour = '#57554f'

                # Determine the appropriate fill color based on the color_value
                for threshold, color in colour_ranges:
                    if color_value < threshold:
                        fill_colour = color
                        break

                # Create the rectangle with the determined fill color
                self.create_rectangle(x, y, x + 5, y + 5, fill=fill_colour, outline=fill_colour)



        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                if(forest_map[x, y]): self.create_oval(x-2, y-2, x+7, y+7, fill="forest green", outline="dark green", width = 4)
                if(rockmap[x, y]):
                    self.create_oval(x-2, y-2, x+7, y+7, fill="PeachPuff3", outline="seashell4", width = 2)
                elif(resources[x, y] > 0):
                    self.create_oval(x-2, y-2, x+7, y+7, fill="yellow", outline="red", width = 2)


    def load_settings(self) -> None:
        config:configparser.ConfigParser = configparser.ConfigParser()
        config.read('settings.ini')

        # Load control key from settings.ini (default to 'F' if not specified)
        self.width = config.getint('Map', 'width', fallback = 1200)
        self.height = config.getint('Map', 'height', fallback = 700)