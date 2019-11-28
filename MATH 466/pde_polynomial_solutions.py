from sympy import *

#finds nonzero polynomial solutions to a system of partial differential equations

# declaring base ring
d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10 = symbols('d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10')
base_ring_generators = [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10]
base_ring = QQ.old_poly_ring(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)

# display preferences
init_printing(use_unicode = False, weap_lines = False)

# declaire pde associated ideal
ideal_generators = [d_1*d_2]

def make_ideal_from_generators(generators):
    return base_ring.ideal(*generators)

def saturate(J,I):
    #returns (J:I^∞)
    # return J.saturate(base_ring) not yet implimented in sympy
    X = J.quotient(I)
    I2 = make_ideal_from_generators(power_generators(I.gens(),2))
    Y = J.quotient(I2)
    import pdb; pdb.set_trace()
    if X == Y:
        return make_ideal_from_generators(X)
    else:
        pass


def system_check():
    pass
    # check if the ideal is st J = J' or a generator of J' has a nonzero constant term

    return_gens = []
    for generator in generators:
        return_gens.append((generator)^power)
    return return_gens

R = make_ideal_from_generators(base_ring_generators)
J = make_ideal_from_generators(ideal_generators)

saturate(J,R)
