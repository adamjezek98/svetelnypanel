import sys, pygame
pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

height = 500
width = 480

screen = pygame.display.set_mode((width, height))

margin = 10
space = 2

matrix = [  [green,  green,  green,  blue,  green,  pink,  pink,  blue,  blue,  green,  white,  pink,  red,  blue,  white],  
            [pink,  red,  green,  white,  green,  red,  green,  white,  red,  green,  pink,  white,  red,  green,  red],  
            [blue,  pink,  red,  red,  white,  pink,  blue,  green,  pink,  pink,  green,  blue,  green,  white,  pink],  
            [green,  blue,  white,  white,  pink,  blue,  pink,  blue,  pink,  white,  blue,  red,  blue,  pink,  red],  
            [red,  pink,  green,  blue,  blue,  green,  red,  red,  blue,  white,  pink,  green,  blue,  red,  red],  
            [red,  pink,  green,  blue,  white,  green,  blue,  blue,  red,  pink,  green,  green,  white,  green,  red],  
            [red,  pink,  green,  blue,  white,  blue,  white,  white,  white,  green,  pink,  blue,  pink,  pink,  pink],  
            [green,  green,  red,  blue,  green,  blue,  white,  white,  blue,  red,  white,  green,  white,  red,  red],  
            [blue,  green,  green,  white,  green,  red,  pink,  red,  green,  blue,  green,  pink,  white,  red,  red] ]

size = (width-(2*margin + (len(matrix[0])-1)*space))/len(matrix[0])


def drawOnScreen():
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            scrx =margin+x*space+x*size
            scry =margin+y*size+y*space
            pygame.draw.rect(screen, matrix[y][x], (scrx,scry, size, size), 0 )
        
    pygame.display.update()        


import time
cas = int(round(time.time() * 1000))
drawOnScreen()
print int(round(time.time() * 1000)) - cas







