import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


def generate_mountain(heightmap, peak_range):
    peak_position = np.unravel_index(np.argmax(heightmap), heightmap.shape)

    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            distance = np.sqrt((i - peak_position[0])**2 + (j - peak_position[1])**2)
            if distance <= peak_range:
                heightmap[i, j] += int(253 * (1 - distance/peak_range))

    return heightmap