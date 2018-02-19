from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import numpy as np
from math import*


def face():
    glColor(1,0.1,0.5)
    glBegin(GL_POLYGON)
    r = .2
    x0 = 0
    y0 = .55
    for theta in np.arange(0, 2*pi, .001):
        x = x0 + r * cos(theta)
        y =  y0 + r * sin(theta)
        glVertex2d(x,y)
    glEnd()
    glFlush()
def nose():
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    r = .02
    x0 = 0
    y0 = .5
    for theta in np.arange(0, 2 * pi, .001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()

def glass ():
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    r = .04
    x0 = 0.12
    y0 = .59
    for theta in np.arange(0, 2 * pi, .001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()


    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    r = .04
    x0 = -0.12
    y0 = .59
    for theta in np.arange(0, 2 * pi, .001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()
def line():
    glColor(0,0,1)
    glBegin(GL_LINE_STRIP)

    glVertex2d(.09, .59)
    #glVertex2d(.13, .59)
   # glVertex2d(-.10,.5)
    glVertex2d(-.09,.59)
    glEnd()
    #glFlush()

    glColor(0, 0, 1)
    glBegin(GL_LINE_STRIP)

    glVertex2d(.09, .59)
    # glVertex2d(.13, .59)
    # glVertex2d(-.10,.5)
    glVertex2d(-.09, .59)
    glEnd()
    glFlush()

    #RIGHT EYE
    glColor(1,1,1)
    glBegin(GL_POLYGON)
    r = .03
    x0 =.12
    y0 =.59
    for theta in np.arange(0,2*pi,.001):
        x = x0 + r * cos(theta)
        y = y0 + r* sin(theta)
        glVertex2d(x,y)
    glEnd()
    glFlush()

    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = .01
    x0 = .12
    y0 = .59
    for theta in np.arange(0, 2 * pi, .001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()

    #LEFT EYE
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    r = .03
    x0 = -.12
    y0 = .59
    for theta in np.arange(0, 2 * pi,.001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    r = .01
    x0 = -.12
    y0 = .59
    for theta in np.arange(0, 2 * pi, .001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()


def mouse():
    glColor3d(0,1,1)
    glBegin(GL_POLYGON)
    glVertex2d(.07,.4)
    glVertex2d(.07, .45)
    glVertex2d(-.07, .45)
    glVertex2d(-.07, .4)
    glEnd()

def knec_1():
    glColor3d(.1, .2, .5)
    glBegin(GL_POLYGON)
    glVertex2d(.07, .3)
    glVertex2d(.07, .35)
    glVertex2d(-.07, .35)
    glVertex2d(-.07, .3)
    glEnd()

def ears():
    glColor3d(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(.2, .53)
    glVertex2d(.22, .53)
    glVertex2d(.22, .57)
    glVertex2d(.2, .57)
    glEnd()
    glColor3d(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-.2, .53)
    glVertex2d(-.22, .53)
    glVertex2d(-.22, .57)
    glVertex2d(-.2, .57)
    glEnd()


def body():
    glColor3d(0,0,.3)
    glBegin(GL_POLYGON)
    glVertex2d(.3,.3)
    glVertex2d(.3, -.3)
    glVertex2d(-.3,- .3)
    glVertex2d(-.3, .3)
    glEnd()

'''def pocket():
    glColor3d(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2d(.1,-.1)
    glVertex2d(.2, -.1)
    glVertex2d(-.2, .2)
    glVertex2d(-.1, .2)
    glEnd()'''









def legs():
    glColor3d(0,0,.2)
    glBegin(GL_POLYGON)

    glVertex2d(.15, -.3)
    glVertex2d(.25, -.3)
    glVertex2d(.25, -.7)
    glVertex2d(.15, -.7)
    glEnd()

    glColor3d(0,0,.2)
    glBegin(GL_POLYGON)
    glVertex2d(-.15,-.3)
    glVertex2d(-.15, -.7)
    glVertex2d(-.25, -.7)
    glVertex2d(-.25, -.3)
    glEnd()

def hands():
    glColor3d(0,.5,.5)
    glBegin(GL_POLYGON)

    glVertex2d(.3,.3)
    glVertex2d(.7, 0)
    glVertex2d(.65, -.1)
    glVertex2d(.3,.2)
    glEnd()
    glColor3d(0,.5,.5)
    glBegin(GL_POLYGON)
    glVertex2d(-.3,.3)
    glVertex2d(-.7, 0)
    glVertex2d(-.65, -.1)
    glVertex2d(-.3, .2)
    glEnd()


def animi():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    face()
   # pocket()
    body()
    mouse()
    knec_1()
    nose()
    hands()
    legs()
    glass()
    ears()
    line()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700)  # Set the window's initial width & height
glutCreateWindow(b":intial carton man report")
glutDisplayFunc(animi)
glutMainLoop()








