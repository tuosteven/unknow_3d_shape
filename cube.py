# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:49:34 2022

@author: acer
"""

import pygame
from pygame.locals import *
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (0,2,0),
    (2,0,0),
    (0,0,2),
    (-2,0,0),
    (0,-2,0),
    (0,0,-2)
    )

edges = (
    
    (8,1),
    (8,2),
    (8,5),
    (8,7),
    (9,0),
    (9,1),
    (9,5),
    (9,4),
    (10,4),
    (10,5),
    (10,6),
    (10,7),
    (11,2),
    (11,3),
    (11,6),
    (11,7),
    (12,0),
    (12,3),
    (12,4),
    (12,6),
    (13,0),(13,1),(13,2),(13,3)    
    )
"""
(0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
"""
def Cube():
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
key = 0
A=1
def main():
    A=1
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        
        for event in pygame.event.get():
            if cv2.waitKey(1) & 0xFF == ord('s'):
             A = A +1 
             print(A)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        glRotatef(A,1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()