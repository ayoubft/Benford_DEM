"""
This script is for functions that return the distribution of leading digits of a numerical distribution.
Make sure you numerical distribution spans a few orders of magnitude.

Author: ayoubft
"""

def getdld(numd):
    """
    Get the distribution of leading digits of a given numerical distribution
    """
    
    f1, f2, f3, f4, f5, f6, f7, f8, f9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in numd:
        c = str(i)[0]
        if c == '1':
            f1 += 1
        elif c == '2':
            f2 += 1;
        elif c == '3':
            f3 += 1;
        elif c == '4':
            f4 += 1;
        elif c == '5':
            f5 += 1;
        elif c == '6':
            f6 += 1;
        elif c == '7':
            f7 += 1;
        elif c == '8':
            f8 += 1;
        elif c == '9':
            f9 += 1;
        
        
    
    return f1, f2, f3, f4, f5, f6, f7, f8, f9