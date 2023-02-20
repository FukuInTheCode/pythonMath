import pygame as pyg
import numpy as np
from src.objects import Point
from math import cos, sin, pi

class projection_to2d:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
        
    projection_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0]
    ])
    
    
    def __init__(self, screen: pyg.Surface, objs: list[Point]) -> None:
        
        self.win = screen

        self.objects = objs

    def start(self):
        clock = pyg.time.Clock()
        
        angle = 0
        
        while True:
            clock.tick(120)

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    exit()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        pyg.quit()
                        exit()
            
            # update stuff
            
            alpha = cos(angle)
            beta = sin(angle)
            
            xyz_rotation = np.matrix([
                [alpha**2, -1*beta*alpha, beta],
                [beta**2*alpha+beta*alpha, -1*beta**3+alpha**2, -1*beta*alpha],
                [-1*beta*alpha**2+beta**2, -1*beta**2*alpha+beta*alpha, alpha**2]
            ])
            
            angle = (angle + 0.01)%(2*pi)

            self.win.fill(self.WHITE)
            
            for obj in self.objects:
                obj.update(xyz_rotation)
                obj.draw(self.win, 100)
                
            pyg.display.flip()