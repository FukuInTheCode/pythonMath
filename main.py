from src.my_2dProjection import projection_to2d
import pygame as pyg
import numpy as np
from src.objects import Point

def main():
    win = pyg.display.set_mode((720, 500))
    
    p2d = projection_to2d(win, [Point(1, 1, 1)])
    
    p2d.start()


if __name__ == "__main__":  
    main()