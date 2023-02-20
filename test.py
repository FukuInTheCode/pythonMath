import numpy as np
from math import cos, sin, pi


angle = 3

beta = sin(angle)
alpha = cos(angle)


rotation_z = np.matrix([
    [cos(angle), -sin(angle), 0],
    [sin(angle), cos(angle), 0],
    [0, 0, 1],
])

rotation_y = np.matrix([
    [cos(angle), 0, sin(angle)],
    [0, 1, 0],
    [-sin(angle), 0, cos(angle)],
])

rotation_x = np.matrix([
    [1, 0, 0],
    [0, cos(angle), -sin(angle)],
    [0, sin(angle), cos(angle)],
])

xyz_rotation = np.matrix([
                [alpha**2, -1*beta*alpha, beta],
                [beta**2*alpha+beta*alpha, -1*beta**3+alpha**2, -1*beta*alpha],
                [-1*beta*alpha**2+beta**2, -1*beta**2*alpha+beta*alpha, alpha**2]
            ])


print(np.dot(np.dot(rotation_x, rotation_y), rotation_z))

print(xyz_rotation)