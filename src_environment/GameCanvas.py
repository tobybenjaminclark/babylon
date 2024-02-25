from tkinter import *
import numpy as np
import configparser
from src_terrain_generation.bblyn_generate_heightmap import generate_heightmap
from src_terrain_generation.bblyn_generate_forestmap import generate_forestmap
from src_terrain_generation.bblyn_generate_rockmap import generate_rockmap
from src_terrain_generation.bblyn_generate_mountain import generate_mountain

class GameCanvas(Canvas):

    def __init__(self, *args, **kwargs) -> None:
        self.load_settings()
        super().__init__(width=self.width, height=self.height, bg="black", *args, **kwargs)

        self.render_map()

        self.update()

    def render_map(self) -> None:
        # Set the resolution and tileability for the Perlin noise
        shape = (self.width, self.height)
        # Generate Perlin noise
        normalized_map = generate_heightmap((self.width, self.height))

        normalized_map = generate_mountain(normalized_map, 150)
        forest_map = generate_forestmap(normalized_map)
        rockmap = generate_rockmap(normalized_map)


        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Use the Perlin noise values to determine the color
                color_value = int(normalized_map[x, y])

                fill_colour = 'red'
                # Define color ranges
                if 0 <= color_value < 30: fill_colour = 'cyan3'
                elif 30 <= color_value < 60: fill_colour = 'cyan2'
                elif 60 <= color_value < 90: fill_colour = 'aquamarine'
                elif 90 <= color_value < 92: fill_colour = 'NavajoWhite3'
                elif 92 <= color_value < 100: fill_colour = 'NavajoWhite2'
                elif 100 <= color_value < 150: fill_colour = 'olive drab'
                elif 150 <= color_value < 255: fill_colour = 'dark olive green'
                elif 255 <= color_value < 315: fill_colour = 'NavajoWhite3'
                elif 315 <= color_value < 400: fill_colour = 'NavajoWhite4'
                else: fill_colour = 'sienna4'

                # Create the rectangle with the determined fill color
                self.create_rectangle(x, y, x + 5, y + 5, fill=fill_colour, outline=fill_colour)


        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                if(forest_map[x, y]): self.create_oval(x-2, y-2, x+7, y+7, fill="forest green", outline="dark green", width = 4)
                if(rockmap[x, y]):
                    self.create_oval(x-2, y-2, x+7, y+7, fill="PeachPuff3", outline="seashell4", width = 2)


    def load_settings(self) -> None:
        config:configparser.ConfigParser = configparser.ConfigParser()
        config.read('settings.ini')

        # Load control key from settings.ini (default to 'F' if not specified)
        self.width = config.getint('Map', 'width', fallback = 1200)
        self.height = config.getint('Map', 'height', fallback = 700)