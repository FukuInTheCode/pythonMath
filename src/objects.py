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
        self._vector = np.matrix([x, y, z]).reshape(3, 1)
        self.vector = self._vector.copy()
        
    def draw(self, screen: pyg.Surface, scale:int) -> None:
        proj2d = np.dot(self.projection_matrix, self.vector)
        
        x = int(proj2d[0][0] * scale) + screen.get_width()/2
        y = int(proj2d[1][0] * scale) + screen.get_height()/2
                
        pyg.draw.circle(screen, self.RED, (x, y), 5)
        
    def update(self, transform: np.ndarray) -> None:
        self.vector = np.dot(transform, self._vector)
        
        
        
        
class Cube(Point):
    
    def __init__(self, x: int, y: int, z: int, side:int) -> None:
        super().__init__(x, y, z)
        
        self.vertexes = [Point(
            side*(1 if i in (1, 2, 5, 7) else 0) + x,
            side*(1 if i in (3, 2, 6, 7) else 0) + y,
            side*(1 if i in (4, 5, 6, 7) else 0) + z
        ) for i in range(8)]
        
        self._vector = self.vector + side/2
        self.vector = self.vector.copy()
        
    def update(self, transform: np.ndarray) -> None:
        for i in self.vertexes:
            i.update(transform)
            
        return super().update(transform)
            
    def draw(self, screen: pyg.Surface, scale: int) -> None:
        
        for i in self.vertexes:
            i.draw(screen, scale)
        
        return super().draw(screen, scale)
    
    
class Eq_Triangle(Point):
    def __init__(self, x: int, y: int, z: int, ) -> None:
        super().__init__(x, y, z)