import math
import numpy as np
def rotation_layer(X, angle):
    rotation = [[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]]
    return   np.array(X) @ np.array(rotation).T
    pass