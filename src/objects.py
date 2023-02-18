import numpy as np
import pygame as pyg

def matrix_to_array(matrix: np.ndarray, params: tuple[int]) -> tuple[int]:
    return (int(matrix[0])+ params[0], int(matrix[1])+ params[1])


class Point:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    projection_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0]
    ])

    def __init__(self, x: int, y: int, z: int) -> None:
        self.vector = np.matrix([x, y, z]).reshape(3, 1)
        
    def draw(self, screen: pyg.Surface, scale:int) -> None:
        proj2d = np.dot(self.projection_matrix, self.vector)
        
        print(proj2d[0][0])
        x = int(proj2d[0][0] * scale) + screen.get_width()/2
        y = int(proj2d[1][0] * scale) + screen.get_height()/2
        
        pyg.draw.circle(screen, self.RED, (x, y), scale)
        
    def update(self, transform: np.ndarray) -> None:
        self.vector = np.dot(transform, self.vector)
        
                