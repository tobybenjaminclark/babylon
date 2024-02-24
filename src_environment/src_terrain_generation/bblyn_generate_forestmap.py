import numpy as np

def generate_forestmap(heightmap):
    heightmap_array = np.array(heightmap)
    forestmap = np.random.choice([True, False], size=heightmap_array.shape, p=[0.3, 0.7])
    return forestmap