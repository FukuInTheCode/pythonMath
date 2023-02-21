import numpy as np
import pygame as pyg
from math import cos, sin


class Point:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    rotations = {'x': lambda angle: np.matrix([
                        [1, 0, 0],
                        [0, cos(angle), -sin(angle)],
                        [0, sin(angle), cos(angle)],
                    ]),
    
                'y': lambda angle: np.matrix([
                        [cos(angle), 0, sin(angle)],
                        [0, 1, 0],
                        [-sin(angle), 0, cos(angle)],
                ]   ),
    
                'z': lambda angle: np.matrix([
                        [cos(angle), -sin(angle), 0],
                        [sin(angle), cos(angle), 0],
                        [0, 0, 1],
                    ])
                    }
    
    
    projection_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0]
    ])

    def __init__(self, x: int, y: int, z: int, rotation: str = 'zyx', stactic: bool = False, center: np.matrix = np.matrix([0, 0, 0]).reshape(3, 1)) -> None:
        self._vector = np.matrix([x, y, z]).reshape(3, 1)
        self.vector = self._vector.copy()
        
        self.static = stactic
        
        self.rota = rotation
        
        self.attachedPoints = []
        
        self.center = center
        
    def draw(self, screen: pyg.Surface, scale:int) -> None:
        for point in self.attachedPoints:
            pyg.draw.line(screen, self.BLACK, tuple(self.get_tuple(scale=scale, params=(screen.get_size()))), tuple(point.get_tuple(scale=scale, params=(screen.get_size()))))
        
        proj2d = np.dot(self.projection_matrix, self.vector)
        
        x = int(proj2d[0][0] * scale) + screen.get_width()/2
        y = int(proj2d[1][0] * scale) + screen.get_height()/2
        
        pyg.draw.circle(screen, self.RED, (x, y), 5)
        
    def update(self, angle: float) -> None:
        # check if the element can move
        if self.static:
            return
        
        # set the new vector of the point
        rotation_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0], 
            [0, 0, 1]
        ])
        
        for axis in self.rota:
            rotation_matrix = np.dot(rotation_matrix, self.rotations[axis](angle))
            
        self.vector = np.dot(rotation_matrix, self._vector-self.center) + self.center
        
    
    def get_tuple(self, transformation: np.ndarray = np.matrix([[1, 0, 0], [0, 1, 0]]), scale: int = 1, params: tuple = (0, 0, 0)):
        tmp = 0
        for i in np.dot(transformation, self.vector):
            yield float(i[0])*scale + params[tmp]/2
            tmp += 1
            
    def link(self, *ps):
        for p in ps:
            if type(p) is Point:
                self.attachedPoints.append(p)
        
        