import numpy as np

# Function to generate a rock map of true/false values from a heightmap.
def generate_booleanmap(heightmap, num_clusters: int, cluster_density: float, cluster_radius: int, range_lower: int, range_upper: int):
    heightmap_array = np.array(heightmap)
    rockmap = np.zeros_like(heightmap_array, dtype = bool)

    for _ in range(num_clusters):
        cluster_center = np.random.randint(0, heightmap_array.shape[0]), np.random.randint(0, heightmap_array.shape[1])
        indices = np.array(list(np.ndindex(heightmap_array.shape)))
        distances = np.linalg.norm(indices - np.array(cluster_center), axis=1)
        valid_heights = (heightmap_array[indices[:, 0], indices[:, 1]] > range_lower) & (heightmap_array[indices[:, 0], indices[:, 1]] < range_upper)

        probabilities = np.exp(-distances / cluster_radius) * cluster_density
        probabilities *= valid_heights
        rockmap |= np.random.rand(*rockmap.shape) < probabilities.reshape(rockmap.shape)
    return rockmap

# Partial Function Applications to generate features, using booleanmap as a base.
def generate_rockmap(heightmap) -> np.array: return generate_booleanmap(heightmap, 6, 0.05, 150, 80, 95)
def generate_forestmap(heightmap) -> np.array: return generate_booleanmap(heightmap, 6, 0.01, 110, 110, 230)
def generate_bushmap(heightmap) -> np.array: return generate_booleanmap(heightmap, 6, 0.06, 70, 90, 300)

