import pygame
import random
import time
from GUISorts import *

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

width = 960
height = 600
window = pygame.display.set_mode((width,height))
window.fill(black)

nums = []
for i in range(15):
    nums.append(random.randint(1,125))


insertion_sort(nums)
