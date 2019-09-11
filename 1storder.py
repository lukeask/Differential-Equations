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

def runge_kutta(xlength, deltax = 1 , initx = 0, inity = 0):
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

def print_txt(name, xvals, yvals):
    outfile = open(name, "a")
    for x in xvals:
        outputformatted = str(x) + ","
        outfile.write(outputformatted)
    outfile.write("\n")
    for y in yvals:
        outputformatted = str(y) + ","
    outfile.close()

def make_graph(xvals,yvals):
    plt.plot(xvals,yvals)
    plt.show()


def tests(xlength = 10, deltax = 0.1, initx = 0 , inity = 0.5):
    em = eulersmethod(xlength, deltax, initx, inity)
    make_graph(em[0],em[1])
    rk = runge_kutta(xlength, deltax, initx, inity)
    make_graph(rk[0],rk[1])

def compute_all_txt(xlength, deltax, initx, inity):
    em = eulersmethod(xlength, deltax, initx, inity)
    rk = runge_kutta(xlength, deltax, initx, inity)
    eulername = "eapx:" + str(deltax) + "(" + str(initx) + ", "+ str(inity) + ")"
    rkname = "rkapx:" + str(deltax) + "(" + str(initx) + ", "+ str(inity) + ")"
    print_txt(eulername, em[0], em[1])
    print_txt(rkname, rk[0], rk[1])

def outmain():
    compute_all_txt()


outmain()
