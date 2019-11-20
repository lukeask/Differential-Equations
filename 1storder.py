import numpy as np
import matplotlib.pyplot as plt
import math

#optional exact equation
def exacteq(x):
    return 1/(1-(math.sin(x)*math.cos(x)))

def exactmethod(xlength, deltax, initx, inity):
    xvals = [initx]
    yvals = [inity]
    for _ in range(int(xlength/deltax)):
        inity = exacteq(initx)
        initx = initx + deltax
        xvals.append(initx)
        yvals.append(inity)
    #import pdb; pdb.set_trace()
    return(xvals, yvals)

# input differential equation in the form of y' = f(x,y)
def deriv(x,y):
    #return y' from x,y
    return y*y*math.cos(2*x)


#implimentation of euler's method
def eulersmethod(xlength, deltax = 1, initx = 0, inity = 0):
    xvals = [initx]
    yvals = [inity]
    for _ in range(int(xlength/deltax)):
        inity = inity + deriv(initx, inity) * deltax
        initx = initx + deltax
        xvals.append(initx)
        yvals.append(inity)
    return(xvals, yvals)


# Runge Kutta method for aproximating a differential equation
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


# outputs two lists to a text file with excel formatting
def print_txt(name, xvals, yvals):
    outfile = open(name, "a")
    for x in xvals:
        outputformatted = str(x) + ","
        outfile.write(outputformatted)
    outfile.write(";")
    for y in yvals:
        outputformatted = str(y) + ","
        outfile.write(outputformatted)
    outfile.close()


# displays a graph given x and y coordinate lists
def make_graph(xvals,yvals, name = 'Figure'):
    plt.scatter(xvals,yvals)
    plt.title(name)
    plt.show()


# displays graphs for numerical methods
def tests(xlength = 10, deltax = 0.1, initx = 0 , inity = 0.5):
    em = eulersmethod(xlength, deltax, initx, inity)
    make_graph(em[0],em[1])
    rk = runge_kutta(xlength, deltax, initx, inity)
    make_graph(rk[0],rk[1])


# outputs all implimented numerical methods to text files
def compute_all_txt(xlength, deltax, initx, inity):
    em = eulersmethod(xlength, deltax, initx, inity)
    rk = runge_kutta(xlength, deltax, initx, inity)
    eulername = "eapx" + str(deltax) + "(" + str(initx) + ", "+ str(inity) + ").txt"
    rkname = "rkapx" + str(deltax) + "(" + str(initx) + ", "+ str(inity) + ").txt"
    print_txt(eulername, em[0], em[1])
    print_txt(rkname, rk[0], rk[1])


def generate_all_plots(xlength, deltax, initx, inity):
    em = eulersmethod(xlength, deltax, initx, inity)
    rk = runge_kutta(xlength, deltax, initx, inity)
    ename = "Euler's Method with Step Size " + str(deltax)
    rkname = "Runge Kutta Method with Step Size" + str(deltax)
    #make_graph(em[0], em[1], ename)
    make_graph(rk[0], rk[1], rkname)


# computes outputs for lab requirements
def outmain():
    compute_all_txt(50, 0.1, 0, 0.1)
    compute_all_txt(50, 0.18, 0, 0.1)
    compute_all_txt(50, 0.23, 0, 0.1)
    compute_all_txt(50, 0.25, 0, 0.1)
    compute_all_txt(50, 0.3, 0, 0.1)


# generates plots for lab requirements
def plotmain():
    generate_all_plots(50, 0.1, 0, 0.1)
    generate_all_plots(50, 0.18, 0, 0.1)
    generate_all_plots(50, 0.23, 0, 0.1)
    generate_all_plots(50, 0.25, 0, 0.1)
    generate_all_plots(50, 0.3, 0, 0.1)


def plotvsexact(h = 0.4):
    em = eulersmethod(6, h, 0, 1)
    xvals = em[0]
    yvals = em[1]
    max_error = 0
    #import pdb; pdb.set_trace()
    for i in enumerate(xvals):
        temp = ((xvals[i[0]]-yvals[i[0]])**2)**(0.5)
        if temp >= max_error:
            max_error = temp
    exm = exactmethod(6, h, 0, 1)
    #import pdb; pdb.set_trace()
    xvals = xvals + exm[0]
    yvals = yvals + exm[1]
    print(max_error)
    make_graph(xvals, yvals, "y' = y^2cos(2x) Euler h = " + str(h))

for i in range(8):
    plotvsexact(0.5/(2**i))
