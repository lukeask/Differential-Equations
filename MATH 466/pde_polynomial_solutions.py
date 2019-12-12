from sympy import *

#finds nonzero polynomial solutions to a system of partial differential equations

# declaring base ring
d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10 = symbols('d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10')
base_ring_generators = [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10]
base_ring = QQ.old_poly_ring(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)

# display preferences
init_printing(use_unicode = False, weap_lines = False)

# declaire pde associated ideal
ideal_generators = [d_1+d_2+d_3, d_1*d_2]
#[d_1+d_2+d_3+1, d_1*d_2+d_1*d_3+d_2*d_3-4, d_1*d_2*d_3]

def make_ideal_from_generators(generators):
    return base_ring.ideal(*generators)

def power_generators(generators, n):
    newgens = []
    for gen in generators:
        newgens.append(gen**n)
    return base_ring.ideal(*newgens)

def saturate(J,I):
    #returns (J:I^∞)
    # return J.saturate(base_ring) not yet implimented in sympy
    n = 2
    running_ideal = J.quotient(I)
    while True:
        colon = J.quotient(I)
        colon_higher = J.quotient(power_generators(base_ring_generators,n))
        if colon == colon_higher:
            return running_ideal
        else:
            running_ideal = running_ideal.union(colon)
            colon = colon_higher

def system_check():
    pass
    # check if the ideal is st J = J' or a generator of J' has a nonzero constant term


if __name__ == "__main__":
    R = make_ideal_from_generators(base_ring_generators)
    J = make_ideal_from_generators(ideal_generators)

    J_prime = J.quotient(saturate(J,R))
    if I == J_prime:
        print("Error, J = J'")
    else:
        print(J_prime)
