from src.my_2dProjection import projection_to2d
import pygame as pyg
from src.objects import Point, Cube

def main():
    win = pyg.display.set_mode((720, 500))
    
    p2d = projection_to2d(win, [Cube(-1, -1, -1, 2)])
    
    p2d.start()


if __name__ == "__main__":  
    main()