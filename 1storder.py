import numpy as np
import matplotlib.pyplot as plt

def deriv(x,y):
    #return y' from x,y
    return 10*y*(1-y)

def eulersmethod(xlength, deltax = 1, initx = 0, inity = 0):
    xvals = [initx]
    yvals = [inity]
    for _ in range(int(xlength/deltax)):
        inity = inity + deriv(initx, inity) * deltax
        initx = initx + deltax
        xvals.append(initx)
        yvals.append(inity)
    return(xvals, yvals)

def runge_kutta(xlength, deltax = 1 , initx = 0 inity = 0)

eulersmethod(50,0.001,0,0.5)
