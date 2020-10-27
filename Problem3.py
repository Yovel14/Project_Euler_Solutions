from sympy import isprime
from math import sqrt
def LargestPrimeFactor(n):
    if isprime(n):
        return -1
    sq = int(sqrt(n))
    for i in range(sq if sq%2==1 else sq-1,2,-2):#sq if sq%2==1 else sq-1
        if n%i==0 and isprime(i):
            return i
    return -1
print(LargestPrimeFactor(600851475143))