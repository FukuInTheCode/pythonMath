from src.my_2dProjection import projection_to2d
import pygame as pyg
from src.objects import Point, Cube, BasePyramid

def main():
    win = pyg.display.set_mode((720, 500))
    
    p2d = projection_to2d(win, [BasePyramid(-i, -i, -i, 2*i) for i in [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 1]])
    
    p2d.start()


if __name__ == "__main__":  
    main()