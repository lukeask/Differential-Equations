import cmath
import math

class Equation:
    def __init__(self, function, derivative):
        self.eq = function
        self.deriv = derivative

    #compute a complex zero from initial value
    def newtonsmethod(self, xinit, maxiters = 1000, yerror = 0.00000001):
        xnew = xinit
        for i in range(maxiters):
            xnew = xnew - (self.eq(x = xnew)/self.deriv(xnew))
            measurederror = self.eq(x = xnew)
            error_modulus = pow(pow(measurederror.real, 2) + pow(measurederror.imag, 2), 0.5)
            #check result
            if error_modulus < yerror:
                break

        return xnew, error_modulus

class PolynomialEquation(Equation):
    def __init__(self, function, derivative, degree, largest_coeff = 100000):
        super().__init__(function, derivative)
        self.degree = degree
        self.largest_coeff = largest_coeff

    def findallzeros(self, angles = 50, pts_per_dir = 20, same_value_cutoff = 0.001, output_cutoff = 0.001):
        search_radius = self.largest_coeff + 1
        allzeros = []

        #get starting values
        for i in range(angles):
            angle = i*2*3.14159265358979323846/angles
            for k in range(pts_per_dir):
                this_radius = k * search_radius / pts_per_dir
                #creates point and checks newton's method for solution
                c_point = complex(this_radius*math.cos(angle), this_radius*math.sin(angle))
                soln = self.newtonsmethod(c_point)
                if soln[1] < output_cutoff:
                    allzeros.append(self.newtonsmethod(c_point)[0])

        #sorts for duplicates
        i = 0
        while len(allzeros) > self.degree:
            i += 1
            for zero2 in range(len(allzeros)):
                for zero3 in range(len(allzeros)):
                    try:
                        if pow((allzeros[zero2]-allzeros[zero3]).real,2) + pow((allzeros[zero2]-allzeros[zero3]).real,2) < same_value_cutoff:
                            allzeros.pop(zero2)
                    except:
                        pass
            same_value_cutoff = same_value_cutoff * 1.1
            output_cutoff = output_cutoff * 0.9
            if len(allzeros) >= self.degree or i > 1000000:
                import pdb; pdb.set_trace()
                return allzeros






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
    x = indicialeq.findallzeros()
    print(len(x))
    print(x)
