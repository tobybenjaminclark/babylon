from tkinter import *
import configparser
from src_terrain_generation.bblyn_generate_heightmap import generate_heightmap
from src_terrain_generation.bblyn_generate_forestmap import generate_forestmap

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
        forest_map = generate_forestmap(normalized_map)

        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Use the Perlin noise values to determine the color
                color_value = int(normalized_map[x, y])

                fill_colour = 'red'
                # Define color ranges
                if 0 <= color_value < 30: fill_colour = 'seagreen3'
                elif 30 <= color_value < 60: fill_colour = 'seagreen2'
                elif 60 <= color_value < 90: fill_colour = 'seagreen1'
                elif 90 <= color_value < 100: fill_colour = 'cornsilk2'
                elif 100 <= color_value < 140: fill_colour = 'yellow green'
                else: fill_colour = 'olive drab'

                # Create the rectangle with the determined fill color
                self.create_rectangle(x, y, x + 5, y + 5, fill=fill_colour, outline=fill_colour)


        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                if(forest_map[x, y]): self.create_oval(x-2, y-2, x+7, y+7, fill="dark green", outline="black")
                


    def load_settings(self) -> None:
        config:configparser.ConfigParser = configparser.ConfigParser()
        config.read('settings.ini')

        # Load control key from settings.ini (default to 'F' if not specified)
        self.width = config.getint('Map', 'width', fallback = 1200)
        self.height = config.getint('Map', 'height', fallback = 700)