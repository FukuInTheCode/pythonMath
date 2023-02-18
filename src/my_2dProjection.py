import pygame as pyg
import numpy as np
from src.objects import Point
from math import cos, sin

class projection_to2d:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    
    def __init__(self, screen: pyg.Surface, objs: list[Point]) -> None:
        
        self.win = screen

        self.objects = objs

    def start(self):
        clock = pyg.time.Clock()
        
        angle = 0
        
        while True:
            clock.tick(60)

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    exit()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        pyg.quit()
                        exit()
            
            # update stuff

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
            # angle += 0.01

            self.win.fill(self.WHITE)
            
            for obj in self.objects:
                obj.update(rotation_z)
                
            for obj in self.objects:
                obj.draw(self.win, 50)