import numpy as np
from scipy.ndimage import label
from collections import deque
import random
from itertools import product

def interpolant(t):
    return t*t*t*(t*(t*6 - 15) + 10)

def generate_perlin_noise_2d(shape, res, tileable=(False, False), interpolant=interpolant):
    """Generate a 2D numpy array of perlin noise.

    Args:
        shape: The shape of the generated array (tuple of two ints).
            This must be a multple of res.
        res: The number of periods of noise to generate along each
            axis (tuple of two ints). Note shape must be a multiple of
            res.
        tileable: If the noise should be tileable along each axis
            (tuple of two bools). Defaults to (False, False).
        interpolant: The interpolation function, defaults to
            t*t*t*(t*(t*6 - 15) + 10).

    Returns:
        A numpy array of shape shape with the generated noise.

    Raises:
        ValueError: If shape is not a multiple of res.
    """
    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]]\
             .transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    if tileable[0]:
        gradients[-1,:] = gradients[0,:]
    if tileable[1]:
        gradients[:,-1] = gradients[:,0]
    gradients = gradients.repeat(d[0], 0).repeat(d[1], 1)
    g00 = gradients[    :-d[0],    :-d[1]]
    g10 = gradients[d[0]:     ,    :-d[1]]
    g01 = gradients[    :-d[0],d[1]:     ]
    g11 = gradients[d[0]:     ,d[1]:     ]
    # Ramps
    n00 = np.sum(np.dstack((grid[:,:,0]  , grid[:,:,1]  )) * g00, 2)
    n10 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]  )) * g10, 2)
    n01 = np.sum(np.dstack((grid[:,:,0]  , grid[:,:,1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
    # Interpolation
    t = interpolant(grid)
    n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
    n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
    return np.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)


def _get_cluster(hmap: np.ndarray, row: int, col: int, threshold: int) -> list[tuple[int, int]]:
    rows, cols = hmap.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = np.zeros((rows, cols), dtype=bool)
    cluster = []

    queue = deque([(row, col)])
    visited[row, col] = True

    while queue:
        current_row, current_col = queue.popleft()
        cluster.append((current_row, current_col))
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if not(0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row, new_col] and hmap[new_row, new_col] < threshold): continue
            queue.append((new_row, new_col))
            visited[new_row, new_col] = True
    return cluster

def clusterize(heightmap_: list[list[int]], coordinates: set[tuple[int, int]] = set(), clusters: list[tuple[int, int]] = []) -> list[tuple[int, int]]:
    heightmap_array = np.array(heightmap_)
    rows, cols = heightmap_array.shape

    for row_index, col_index in product(range(rows), range(cols)):
        if not((row_index, col_index) not in coordinates and heightmap_array[row_index, col_index] < 100): continue 
        coords = _get_cluster(heightmap_array, row_index, col_index, threshold=100)
        coordinates.update(coords)
        clusters.append(coords)
    return clusters

# Function to generate a terrain heightmap, with rivers, mountains using Perlin Noise as a base, uses numpy for faster generation speed.
def generate_heightmap(shape: tuple[int, int], res: tuple[int, int] = (5, 5), tileable: tuple[bool, bool] = (True, True)) -> dict[str:list[list[int]]]:
    perlin_noise = np.interp((perlin_noise := generate_perlin_noise_2d(shape, res, tileable)), (perlin_noise.min(), perlin_noise.max()), (0, 255)).astype(int)
    height_map = np.interp(np.where(perlin_noise < 100, 100 + (100 - perlin_noise), perlin_noise), (perlin_noise.min(), perlin_noise.max()), (0, 255)).astype(int)
    [height_map.__setitem__((row, column), perlin_noise[row, column]) for cluster in (clusterize(perlin_noise)) if (cindex := int(random.randrange(123, 412) * 1.21)) % 10 < 6 for row, column in cluster]
    return height_map