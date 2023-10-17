



def getKQ(p):
    for _k in range (2,10):
        for _q in range (2,10):
            if p-1 == 2 ** _k * _q:
                return _k,_q

def legendre_symbol(a, p):
    # Compute the Legendre symbol (a/p)
    if a % p == 0:
        return 0
    elif pow(a, (p - 1) // 2, p) == 1:
        return 1
    else:
        return -1
    
def first_non_quadratic_residue(n):
    # Iterate through integers to find the first non-quadratic residue modulo n
    for x in range(1, n):
        legendre = legendre_symbol(x, n)
        if legendre == -1:
            return x


def tonelli(a,p,Q,z,k):
    if pow(a,Q,p) == 1:
        return pow(a,(int)((Q+1)/2),p)
    for i in range(k-1):
        if pow(a,pow(2,i) * Q, p) == -1+p:
            aPrime = a * pow(z,(int)(2 **(k-i-1)),p)
            R = tonelli(aPrime,p,Q,z,k)
            return R * pow(z,-1 *pow(2,k-i-2,p),p) % p
    return "NADA" + str(a)
        
#MAIN
p = 13

a = 4
k,Q = getKQ(p)
z = first_non_quadratic_residue(100)
print(a,p,Q,z,k)
print(tonelli(a,p,Q,z,k))