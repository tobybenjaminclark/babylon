import numpy as np

# Function to generate a rock map of true/false values from a heightmap.
def generate_rockmap(heightmap):
    heightmap_array = np.array(heightmap)
    rockmap = np.zeros_like(heightmap_array, dtype = bool)

    num_clusters = 6
    cluster_density = 0.1
    cluster_radius = 150

    for _ in range(num_clusters):
        cluster_center = np.random.randint(0, heightmap_array.shape[0]), np.random.randint(0, heightmap_array.shape[1])
        indices = np.array(list(np.ndindex(heightmap_array.shape)))
        distances = np.linalg.norm(indices - np.array(cluster_center), axis=1)
        valid_heights = (heightmap_array[indices[:, 0], indices[:, 1]] > 85) & (heightmap_array[indices[:, 0], indices[:, 1]] < 99)

        probabilities = np.exp(-distances / cluster_radius) * cluster_density
        probabilities *= valid_heights

        rockmap |= np.random.rand(*rockmap.shape) < probabilities.reshape(rockmap.shape)

    return rockmap
