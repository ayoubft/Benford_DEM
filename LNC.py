"""
Leading Numbers Count
This script is for functions that return the distribution of leading digits of a numerical distribution.
Make sure you numerical distribution spans a few orders of magnitude.

Author: ayoubft
"""


import numpy as np

# Other method: 

#def leadingDigit(x):
#    while x >= 10:
#        x //= 10
#    return x

def get_dln(numd):
    """
    Get the distribution of leading digits of a given numerical distribution
    """
    f=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in numd:
        c = str(int(i))[0]
        if c == '1':
            f[0] += 1
        elif c == '2':
            f[1] += 1;
        elif c == '3':
            f[2] += 1;
        elif c == '4':
            f[3] += 1;
        elif c == '5':
            f[4] += 1;
        elif c == '6':
            f[5] += 1;
        elif c == '7':
            f[6] += 1;
        elif c == '8':
            f[7] += 1;
        elif c == '9':
            f[8] += 1;
          
    return f

def fdln(f):
    """
    Get a list of distributions frequencies
    """
    k = []
    n = sum(f)
    for i in range(len(f)):
        k.append(100*f[i]/n)
    return k
    

def f_lnd(f):
    """
    Format the output
    """
    n = sum(f)
    print("digit | frequency")
    for i in range(len(f)):
        print(f"    {i+1} | {100 * (f[i] / n):6.2f}")
        # "%d: %6.1f%%\n
