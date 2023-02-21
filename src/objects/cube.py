import numpy as np
import pygame as pyg
from math import cos, sin
from src.objects.point import Point

class Cube(Point):
    
    def __init__(self, x: int, y: int, z: int, side:int, rotation: str = 'xyz', static: bool = False) -> None:
        super().__init__(x, y, z, rotation, static)
        
        self.center = self.vector
        
        self.vertexes = [Point(
            side*(1 if i in (1, 2, 5, 6) else 0) + x-side/2,
            side*(1 if i in (2, 3, 6, 7) else 0) + y-side/2,
            side*(1 if i in (4, 5, 6, 7) else 0) + z-side/2,
            rotation, static, self.center
        ) for i in range(8)]
        
       
        
        for j in (0, 2):
            for i in (1, 3, 4+j):
                self.vertexes[j].attachedPoints.append(self.vertexes[i])
                
            for i in (1+j, 4, 6):
                self.vertexes[j+5].attachedPoints.append(self.vertexes[i])

        
        
    def update(self, angle: float) -> None:
        for i in self.vertexes:
            i.update(angle)
            
        return super().update(angle)
            
    def draw_ortho(self, screen: pyg.Surface, scale: int) -> None:
        for i in self.vertexes:
            i.draw_ortho(screen, scale)
        
        return super().draw_ortho(screen, scale)
    
    
    