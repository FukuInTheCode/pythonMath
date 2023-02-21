import numpy as np
import pygame as pyg


class Point:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    projection_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0]
    ])

    def __init__(self, x: int, y: int, z: int, stactic: bool = False) -> None:
        self._vector = np.matrix([x, y, z]).reshape(3, 1)
        self.vector = self._vector.copy()
        
        self.static = stactic
        
        self.attachedPoints = []
        
    def draw(self, screen: pyg.Surface, scale:int) -> None:
        
        for point in self.attachedPoints:
            pyg.draw.line(screen, self.BLACK, tuple(self.get_tuple(scale=scale, params=(screen.get_size()))), tuple(point.get_tuple(scale=scale, params=(screen.get_size()))))
        
        proj2d = np.dot(self.projection_matrix, self.vector)
        
        x = int(proj2d[0][0] * scale) + screen.get_width()/2
        y = int(proj2d[1][0] * scale) + screen.get_height()/2
        
        pyg.draw.circle(screen, self.RED, (x, y), 5)
        
    def update(self, transform: np.ndarray) -> None:
        
        if self.static:
            return
        
        self.vector = np.dot(transform, self._vector)
        
    
    def get_tuple(self, transformation: np.ndarray = np.matrix([[1, 0, 0], [0, 1, 0]]), scale: int = 1, params: tuple = (0, 0, 0)):
        tmp = 0
        for i in np.dot(transformation, self.vector):
            yield float(i[0])*scale + params[tmp]/2
            tmp += 1
            
    def link(self, *ps):
        for p in ps:
            if type(p) is Point:
                self.attachedPoints.append(p)
        
        
        
        
class Cube(Point):
    
    def __init__(self, x: int, y: int, z: int, side:int, static: bool = False) -> None:
        super().__init__(x, y, z)
        
        self.vertexes = [Point(
            side*(1 if i in (1, 2, 5, 6) else 0) + x,
            side*(1 if i in (2, 3, 6, 7) else 0) + y,
            side*(1 if i in (4, 5, 6, 7) else 0) + z,
            static
        ) for i in range(8)]
        
        for j in (0, 2):
            for i in (1, 3, 4+j):
                self.vertexes[j].attachedPoints.append(self.vertexes[i])
                
            for i in (1+j, 4, 6):
                self.vertexes[j+5].attachedPoints.append(self.vertexes[i])
        
                

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
    
    
class BasePyramid(Point):
    def __init__(self, x: int, y: int, z: int, side:int) -> None:
        super().__init__(x, y, z)
        
        self.vertexes = [Point(
                x + side*(1 if i in (1, 2) else (1/2 if i == 4 else 0)),
                y + side*(1 if i in (2, 3) else (1/2 if i == 4 else 0)),
                z + side*(1 if i == 4 else 0)
            ) for i in range(5)]
        
        for vertex in self.vertexes:
            self.vertexes[4].attachedPoints.append(vertex)
            
        for i in (0, 2):
            self.vertexes[i].attachedPoints.append(self.vertexes[1])
            self.vertexes[i].attachedPoints.append(self.vertexes[3])
        
        
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
    