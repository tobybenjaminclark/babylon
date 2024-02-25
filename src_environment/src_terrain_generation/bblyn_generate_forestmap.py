import numpy as np

def generate_forestmap(heightmap):
    heightmap_array = np.array(heightmap)
    forestmap = np.zeros_like(heightmap_array, dtype=bool)

    num_clusters = 6
    cluster_density = 0.5
    cluster_radius = 80

    for _ in range(num_clusters):
        cluster_center = np.random.randint(0, heightmap_array.shape[0]), np.random.randint(0, heightmap_array.shape[1])

        # Generate forest in the surrounding tiles based on the selected center
        indices = np.array(list(np.ndindex(heightmap_array.shape)))
        distances = np.linalg.norm(indices - np.array(cluster_center), axis=1)
        valid_heights = (heightmap_array[indices[:, 0], indices[:, 1]] > 135) & (heightmap_array[indices[:, 0], indices[:, 1]] < 255)

        probabilities = np.exp(-distances / cluster_radius) * cluster_density
        probabilities *= valid_heights

        # Use boolean indexing for updating forestmap
        forestmap |= np.random.rand(*forestmap.shape) < probabilities.reshape(forestmap.shape)

    return forestmap
