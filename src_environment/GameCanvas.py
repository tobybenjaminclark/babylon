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

                # Interpolate between light blue and green
                blue_component = 255 - color_value
                green_component = color_value

                # Ensure the RGB values are in the valid range [0, 255]
                blue_component = max(0, min(255, blue_component))
                green_component = max(0, min(255, green_component))

                fill_color = f'#00{green_component:02x}{blue_component:02x}'

                
                if(forest_map[x, y]): self.create_rectangle(x, y, x + 5, y + 5, fill="lime", outline="lime")
                else: self.create_rectangle(x, y, x + 5, y + 5, fill=fill_color, outline=fill_color)


    def load_settings(self) -> None:
        config:configparser.ConfigParser = configparser.ConfigParser()
        config.read('settings.ini')

        # Load control key from settings.ini (default to 'F' if not specified)
        self.width = config.getint('Map', 'width', fallback = 1200)
        self.height = config.getint('Map', 'height', fallback = 700)