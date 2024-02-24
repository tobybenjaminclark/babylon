import numpy as np

# Function to generate two-dimensional perlin noise. Based on 'https://github.com/pvigier/perlin-numpy/blob/master/perlin_numpy/perlin2d.py'
def generate_perlin(shape, res, tileable=(False, False)):
    interpolant = lambda t: t * t * t * (t * (t * 6 - 15) + 10)
    delta, d = (res[0] / shape[0], res[1] / shape[1]), (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]].transpose(1, 2, 0) % 1

    angles = 2 * np.pi * np.random.rand(res[0] + 1, res[1] + 1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))

    if tileable[0]: gradients[-1, :] = gradients[0, :]
    if tileable[1]: gradients[:, -1] = gradients[:, 0]
        
    gradients = np.tile(gradients.repeat(d[0], 0).repeat(d[1], 1), (1, 1, 1))
    g00, g10, g01, g11 = gradients[:-d[0], :-d[1]], gradients[d[0]:, :-d[1]], gradients[:-d[0], d[1]:], gradients[d[0]:, d[1]:]

    n00 = np.sum(np.dstack((grid[:,:,0], grid[:,:,1])) * g00, 2)
    n10 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)

    t = interpolant(grid)
    n0 = n00 * (1 - t[:,:,0]) + t[:,:,0] * n10
    n1 = n01 * (1 - t[:,:,0]) + t[:,:,0] * n11

    return np.sqrt(2) * ((1 - t[:,:,1]) * n0 + t[:,:,1] * n1)
