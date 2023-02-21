from src.my_2dProjection import projection_to2d
import pygame as pyg
from src.objects import Point, Cube, BasePyramid
import numpy as np

def main():
    win = pyg.display.set_mode((720, 500))
    
    objects = [Cube(-10, -1, -1, 2, 'xyzxyz')]
    
    p2d = projection_to2d(win, objects)
    
    p2d.start()


if __name__ == "__main__":  
    main()