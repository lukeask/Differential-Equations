def convert_to_d_poly(vector):
    return d_1**vector[0]*d_2**vector[1]*d_3**vector[2]*d_4**vector[3]*d_5**vector[4]

def convert_to_x_poly(vector):
    return x_1**vector[0]*x_2**vector[1]*x_3**vector[2]*x_4**vector[3]*x_5**vector[4]

def get_fact_sum(vector):
    return factorial(vector[0]) + factorial(vector[1]) + factorial(vector[2]) + factorial(vector[3]) + factorial(vector[4])

# Goal: compute the colon ideal I
P.<d_1,d_2,d_3,d_4,d_5> = PolynomialRing(QQ,5,order='lex')
J = P.ideal(d_1*d_3,d_1*d_4, d_2*d_4, d_2*d_5, d_3*d_5, d_1 + d_2 - d_4, d_2 + d_3 - d_5)
R = P.ideal(d_1,d_2,d_3,d_4,d_5)
J_prime = J.saturation(R)[0]


#Goal: Test for finite dimensionality of solution space
    #if J_prime.constant_coefficient() == 0 or J == J_prime:
    #    print("Error, nonzero constant coefficient for J', so the polynomial solutions to J are not finite dimensional")
    #


#Goal: Compute I,G, and in(I)
I = J.quotient(J_prime)
G = I.groebner_basis()

leading_monomials = []
for i in range(len(G)):
    leading_monomials.append(G[i].lm())

#todo add alpha search restrictions

#Goal: find beta
inI = P.ideal(*leading_monomials)
#normal basis has something to do with Galois Extentions, but happens to return exactly what we need
#otherwise calculation can proceed as in poster
inI_basis = inI.normal_basis()
beta = []
for operator in inI_basis:
    beta.append(vector(ZZ, [operator.degree(d_1), operator.degree(d_2), operator.degree(d_3), operator.degree(d_4), operator.degree(d_5)]))


# Goal: find all nonstandard monomials d^alpha
candidates_for_alpha = []
    # create a list of candidates, 20 a temp value to be determined by the ideal I.
    # Maximum value should be the highest monomial coefficient in lm(I)
for i in range(20):
    for value in WeightedIntegerVectors(i, [1,1,1,1,1]):
        candidates_for_alpha.append(value)
candidates_for_alpha = list(set(candidates_for_alpha))
a_cand_d_rep = [d_1^a[0] * d_2^a[1] * d_3^a[2] * d_4^a[3] * d_5^a[4] for a in candidates_for_alpha]

alpha_d_poly = []
for cand in a_cand_d_rep:
    # not element of I
    if cand.reduce(G) != 0:
        # not element of in(I)
        if cand.reduce(inI) == 0:
            alpha_d_poly.append(cand)
alpha = []
for operator in alpha_d_poly:
    alpha.append(vector(ZZ, [operator.degree(d_1), operator.degree(d_2), operator.degree(d_3), operator.degree(d_4), operator.degree(d_5)]))


#Goal: find coefficients for normal forms

#TODO , Sage weird about recursion with vectors
def next_beta(current_beta):
    return_beta = []
    for b in current_beta:
        return_beta.append(b)
        for x in current_beta:
            return_beta.append(b+x)
    return set(list(return_beta))

#currently, this searches linear combinations of beta values with each alpha value
#ideally, this would be done by taking alpha modulo G but that command doesn't return remainders in sage
#if this method is to be generalized, linear combination coefficients based on ideal generators should be used

#making a larger list of polynomials in beta
expanded_beta = []
for b in beta:
    current_poly = convert_to_d_poly(b)
    expanded_beta.append(current_poly)
    expanded_beta.append(-1*current_poly)

#searches expanded beta for elements in the ideal, adds them to beta_alpha, misses alpha = d_2 currently
beta_alpha = []
i = 1
while len(beta_alpha) < len(alpha):
    for value in WeightedIntegerVectors(i, [1]*len(expanded_beta)):
        i+=1
        for a in alpha:
            test_poly = convert_to_d_poly(a)
            for i in range(len(value)):
                test_poly += value[i]*expanded_beta[i]
            if test_poly in I:
                beta_sum = test_poly - convert_to_d_poly(a)
                beta_alpha.append([beta_sum, a])

#condenses results into a sorted list
sorted_b_a = []
mylist = []
for b_a in beta_alpha:
    alph = convert_to_d_poly(b_a[0])
    if alph in mylist:
        pass
    else:
        sorted_b_a.append(b_a)
        mylist.append(alph)
