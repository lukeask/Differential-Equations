import cmath
import math

#tracks useful equation information
class Equation:
    def __init__(self, function, derivative):
        self.eq = function
        self.deriv = derivative


    #compute a complex zero from initial value, returns 0 location and error
    def newtonsmethod(self, xinit, maxiters = 1000, yerror = 0):
        xnew = xinit
        for i in range(maxiters):
            xnew = xnew - (self.eq(x = xnew)/self.deriv(xnew))
            measurederror = self.eq(x = xnew)
            error_modulus = pow(pow(measurederror.real, 2) + pow(measurederror.imag, 2), 0.5)
            #check result
            if error_modulus < yerror:
                break
        return [xnew, error_modulus]


    def makederiv():
        pass
        #todo



# added functionality for polynomial equations
class PolynomialEquation(Equation):
    def __init__(self, function, derivative, degree, largest_coeff):
        super().__init__(function, derivative)
        self.degree = degree
        self.largest_coeff = largest_coeff


    #returns all zeros
    def find_all_zeros(self, angles, pts_per_dir):
        #upper bound for modulus
        search_radius = self.largest_coeff + 1
        allzeros = []
        #get starting values
        for i in range(angles):
            angle = i*2*3.14159265358979323846/angles
            for k in range(pts_per_dir):
                this_radius = k * search_radius / pts_per_dir
                #creates point and checks newton's method for solution
                c_point = complex(this_radius*math.cos(angle), this_radius*math.sin(angle))
                allzeros.append(self.newtonsmethod(c_point)[0])
        return allzeros
        # Output in the form allzeros[zeroindex][0:[z]  1: f[z]]


    def sort_all_zeros(self, zero_list, function_error_cutoff, same_zero_cutoff):
        #no guerentees
        close_list = []
        for zero in zero_list:
            if abs(self.eq(zero)) < function_error_cutoff:
                close_list.append(zero)

        reduced_list = [close_list[0]]

        for zero in close_list:
            i = 0
            while i <= len(reduced_list):
                if i == len(reduced_list):
                    reduced_list.append(zero)
                if abs(zero - reduced_list[i]) < same_zero_cutoff:
                    break
                else:
                    i+=1
        return reduced_list


    def get_zeros(self, angles = 10, pts_per_dir = 10, same_zero_cutoff = 0.01, function_error_cutoff = 0.01):
        zerolist = self.find_all_zeros(angles, pts_per_dir)
        return self.sort_all_zeros(zerolist, function_error_cutoff, same_zero_cutoff)


#creates a PolynomialEquation object with user input
#Requires standard form input
def polypacker(equationname = "Polynomial Equation", var = "setvar"):
    if var == "setvar":
        var = input("{} Variable}: ".format(equationname))
    deg = input("{} Degree: ".format(equationname))

    coefficient = []

    for power in range(int(deg)+1):
        maxcoeff = 0
        coeff = (input("What is the coefficient of {} ^ {}: ".format(var, power)))
        if float(coeff) > maxcoeff:
            maxcoeff = float(coeff)
        try: coefficient.append(int(coeff))
        except:coefficient.append(float(coeff))


    def polyeq(x):
        result = 0
        for i in range(int(deg)+1):
            result = result + coefficient[i]*pow(x,i)
        return result

    def deriveq(x):
        result = 0
        for i in range(1, int(deg)+1):
            result = result + coefficient[i]*pow(x,i-1)*i
        return result

    return PolynomialEquation(polyeq, deriveq, int(deg), maxcoeff)


if __name__ == "__main__":
    indicialeq = polypacker("Indicial Equation", "r")
    print(indicialeq.get_zeros())
