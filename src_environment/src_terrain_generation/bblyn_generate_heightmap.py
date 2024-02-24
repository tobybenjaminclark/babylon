from src_terrain_generation.bblyn_perlin import generate_perlin
import numpy as np
from collections import deque
from itertools import product
import random



# Auxillary Function allowing `_get_cluster` to process neighbouring cells.
def _process_neighbor(dr, dc, current_row, current_col, rows, cols, visited, hmap, threshold, queue):
    new_row, new_col = current_row + dr, current_col + dc
    if not(0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row, new_col] and hmap[new_row, new_col] < threshold): return
    queue.append((new_row, new_col))
    visited[new_row, new_col] = True



# Auxillary Function allowing `_clusterize` to get a specific cluster, using a breadth-first-search approach.
def _get_cluster(hmap: np.ndarray, row: int, col: int, threshold: int) -> list[tuple[int, int]]:
    rows, cols = hmap.shape
    visited = np.zeros((rows, cols), dtype=bool)
    queue, cluster, visited[row, col]  = deque([(row, col)]), [], True
    while queue:
        current_row, current_col = queue.popleft()
        cluster.append((current_row, current_col))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: _process_neighbor(dr, dc, current_row, current_col, rows, cols, visited, hmap, threshold, queue)
    return cluster



# Function to break a heightmap into separate clusters satisfying a threshold, returning lists of connected cluster coordinates.
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
    perlin_noise = np.interp((perlin_noise := generate_perlin(shape, res, tileable)), (perlin_noise.min(), perlin_noise.max()), (0, 255)).astype(int)
    height_map = np.interp(np.where(perlin_noise < 100, 100 + (100 - perlin_noise), perlin_noise), (perlin_noise.min(), perlin_noise.max()), (0, 255)).astype(int)
    [height_map.__setitem__((row, column), perlin_noise[row, column]) for cluster in (clusterize(perlin_noise)) if (cindex := int(random.randrange(123, 412) * 1.21)) % 10 < 6 for row, column in cluster]
    return height_map

