# Calculation of Pi in python according to the Leibniz rule

import time

def calcPi(n):
    pi,numer = 0,4.0
    for i in range(n):
        denom = (2*i+1)
        term = numer/denom
        if (i%2 == 1):
            pi -= term
        else:
            pi += term
    return(pi)

terms = 1000

start_time = time.time()
pi = calcPi(terms)
elapsed_time = (time.time() - start_time) * 1000

print("PI: ", pi)
print("Elapsed Time (Python): ", elapsed_time, "ms")