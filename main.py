from src.my_2dProjection import projection_to2d
import pygame as pyg
from src.objects.point import Point
from src.objects.cube import Cube
from src.objects.basePyramid import BasePyramid
import numpy as np

def main():
    win = pyg.display.set_mode((720, 500))
    
    objects = [BasePyramid(1, 0, 0, 2, 'zy')]
    
    p2d = projection_to2d(win, objects)
    
    p2d.start()


if __name__ == "__main__":  
    main()