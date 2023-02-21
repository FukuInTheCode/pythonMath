import numpy as np
import pygame as pyg
from math import cos, sin
from src.objects.point import Point


class BasePyramid(Point):
    def __init__(self, x: int, y: int, z: int, side:int, rotation: str = 'xyz', static:bool = False) -> None:
        super().__init__(x, y, z, rotation, static)
        
        self.vertexes = [Point(
                x-side/2 + side*(1 if i in (1, 2) else (1/2 if i == 4 else 0)),
                y-side/2 + side*(1 if i in (2, 3) else (1/2 if i == 4 else 0)),
                z-side/2 + side*(1 if i == 4 else 0), 
                rotation, static
            ) for i in range(5)]
        
        for vertex in self.vertexes:
            self.vertexes[4].attachedPoints.append(vertex)
            
        for i in (0, 2):
            self.vertexes[i].attachedPoints.append(self.vertexes[1])
            self.vertexes[i].attachedPoints.append(self.vertexes[3])
            
        
        
    def update(self, angle: float) -> None:
        for i in self.vertexes:
            i.update(angle)
            
        return super().update(angle)
    
    def draw(self, screen: pyg.Surface, scale: int) -> None:
        
        for i in self.vertexes:
            i.draw(screen, scale)
        
        return super().draw(screen, scale)