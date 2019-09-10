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

def runge_kutta(xlength, deltax = 1 , initx = 0 inity = 0):
    xvals = [initx]
    yvals = [inity]
    for _ in range(int(xlength/deltax)):
        k1 = deriv(initx, inity)
        k2 = deriv(initx + (deltax / 2), inity + k1*(deltax / 2))
        k3 = deriv(initx + (deltax / 2), inity + k2*(deltax / 2))
        k4 = deriv(initx + deltax, inity + k3*deltax)
        m = (k1 + 2*k2 + 2*k3 +k4)/6
        inity = inity + (m* deltax)
        initx = initx + deltax
        xvals.append(initx)
        yvals.append(inity)
    return(xvals, yvals)

eulersmethod(50,0.001,0,0.5)
