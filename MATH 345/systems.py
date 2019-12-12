import math
#temporarily only allows for 2 functions
#todo: impliment systems of k functions of n variables
def x_1_prime(one, two, t):
    return (one*two)**2*math.exp(-(one**2+two**2)*0.25)+5*math.cos(two)*math.sin(t)/(two**2+1)

def x_2_prime(one, two, t):
    return 3*math.cos(two**2)/((t**2+1)*(two**2+1))


x_1_init = 5
x_2_init = -1
h = 0.1
t_init = 0
t_end = 3
print(x_1_init,x_2_init,t_init)

while t_init <= t_end:
    I_1_1 = x_1_prime(x_1_init, x_2_init, t_init)
    I_1_2 = x_2_prime(x_1_init, x_2_init, t_init)
    I_2_1 = x_1_prime(x_1_init+I_1_1*(h/2), x_2_init+I_1_2*(h/2), t_init+(h/2))
    I_2_2 = x_2_prime(x_1_init+I_1_1*(h/2), x_2_init+I_1_2*(h/2), t_init+(h/2))
    I_3_1 = x_1_prime(x_1_init+I_2_1*(h/2), x_2_init+I_2_2*(h/2), t_init+(h/2))
    I_3_2 = x_2_prime(x_1_init+I_2_1*(h/2), x_2_init+I_2_2*(h/2), t_init+(h/2))
    I_4_1 = x_1_prime(x_1_init+I_3_1*(h), x_2_init+I_2_2*(h), t_init+(h))
    I_4_2 = x_1_prime(x_1_init+I_3_1*(h), x_2_init+I_2_2*(h), t_init+(h))
    I_1_avg = (I_1_1 + 2*I_2_1 + 2* I_3_1 + I_4_1)/6
    I_2_avg = (I_1_2 + 2*I_2_2 + 2* I_3_2 + I_4_2)/6


    x_1_init = x_1_init+I_1_avg*h
    x_2_init = x_2_init+I_2_avg*h
    t_init = t_init + h
    print(x_1_init,x_2_init,t_init)
