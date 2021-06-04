"""
This 
Leading Numbers Count functions
This script is for functions that return and manipulate the distribution of leading digits of a numerical distribution.
Make sure you numerical distribution spans a few orders of magnitude.

Author: ayoubft
"""

# Import needed libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def leading_digit(x):
    """Get the first digit in a positive number

    Args:
        x (float): POSITIVE float

    Returns:
        int: one digit from 1 to 9
    """    
    # loop until you get the leading digit
    while x >= 10:
        x //= 10
    return x

def count_leading_digits(numd):
    """Get the distribution of leading digits of a given numerical distribution

    Args:
        numd (array of floats): [numpy]array of the numbers

    Returns:
        array of ints: repartition of first digit numbers in numd
    """
    # Initialize the repartition by ones to avoid division by zero error further ahead
    f=[1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    for i in numd:
        c = leading_digit(i)
        if c == 1:
            f[0] += 1
        elif c == 2:
            f[1] += 1
        elif c == 3:
            f[2] += 1
        elif c == 4:
            f[3] += 1
        elif c == 5:
            f[4] += 1
        elif c == 6:
            f[5] += 1
        elif c == 7:
            f[6] += 1
        elif c == 8:
            f[7] += 1
        elif c == 9:
            f[8] += 1
          
    return f

def count_leading_digits_var2(numd):
    """Get the distribution of leading digits of a given numerical distribution

    Args:
        numd (array of floats): [numpy]array to hold the distribution of numbers

    Returns:
        array of ints: repartition of first digit numbers in numd
    """

    # Initialize the repartition by ones to avoid division by zero error further ahead
    f=[1, 1, 1, 1, 1, 1, 1, 1, 1]
    
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

def frequency_leading_digits(f):
    """Get a list of distributions frequencies

    Args:
        f (array of ints): The repartition of first digits of a given distribution

    Returns:
        array of floats: The distribution of leading digits summed to 100%
    """
    
    k = []
    n = sum(f)
    for i in range(len(f)):
        k.append(100*f[i]/n)
    return k
    

def print_distribution_leading_digits(f):
    """Format the output

    Args:
        f (array of floats): The frequencies of distributiion of leading digits
    """ 

    n = sum(f)
    print("digit | frequency")
    print("------|----------")
    for i in range(len(f)):
        print(f"    {i+1} | {100 * (f[i] / n):6.2f}")
        # "%d: %6.1f%%\n


# X (ints): 1 to 9 integers
X = np.arange(1,  10)
# B (array of floats): distribution of Benford
B = 100 * np.log10(1 + (1 / X))

def plot_benford(ff1, ff2, ff3):
    """This function is to automate plotting Benford distributions 

    Args:        
        ff1 (array of floats): distribution of the DEM
        ff2 (array of floats): distribution of the SLOPE
        ff3 (array of floats): distribution of the ASPECT
    """    
    
    # Plotting both the curves simultaneously
    plt.figure(figsize=(15, 12))
    plt.plot(X, B, '--', color='r', label='Benford', linewidth=8)
    plt.plot(X, ff1, color='g', label='DEM', linewidth=5)
    plt.plot(X, ff2, color='b', label='SLOPE', linewidth=5)
    plt.plot(X, ff3, color='y', label='ASPECT', linewidth=5)

    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("Leading Digit", fontsize=20)
    plt.xticks(fontsize = 22)
    plt.ylabel("Percentage", fontsize=20)
    plt.yticks(fontsize = 22)
    plt.title("Leading Digits Distributions", fontsize=28)

    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend(fontsize=18)

    # To load the display window
    plt.show()
    

def plot_benford4(ff1, ff2, ff3, ff4):
    """This function is to automate plotting Benford distributions 

    Args:        
        ff1 (array of floats): distribution of the DEM
        ff2 (array of floats): distribution of the SLOPE
        ff3 (array of floats): distribution of the ASPECT
        ff4 (array of floats): distribution of the STRAHLER ORDER
    """    
    
    # Plotting both the curves simultaneously
    plt.figure(figsize=(15, 12))
    plt.plot(X, B, '--', color='r', label='Benford', linewidth=8)
    plt.plot(X, ff1, color='g', label='DEM', linewidth=5)
    plt.plot(X, ff2, color='b', label='SLOPE', linewidth=5)
    plt.plot(X, ff3, color='y', label='ASPECT', linewidth=5)
    plt.plot(X, ff4, color='k', label='STRAHLER', linewidth=5)

    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("Leading Digit", fontsize=20)
    plt.xticks(fontsize = 22)
    plt.ylabel("Percentage", fontsize=20)
    plt.yticks(fontsize = 22)
    plt.title("Leading Digits Distributions", fontsize=28)

    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend(fontsize=18)

    # To show the plot
    plt.show()
