import numpy as np
from math import cos, sin, pi


angle = 1

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


a = lambda angle: np.matrix([
                [cos(angle)**2, -1*sin(angle)*cos(angle), sin(angle)],
                [sin(angle)**2*cos(angle)+beta*cos(angle), -1*sin(angle)**3+cos(angle)**2, -1*sin(angle)*cos(angle)],
                [-1*sin(angle)*cos(angle)**2+sin(angle)**2, -1*sin(angle)**2*cos(angle)+sin(angle)*cos(angle), cos(angle)**2]
            ])

a = [i for i in 'xyz']

print(a)