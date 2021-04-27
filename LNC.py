"""
Leading Numbers Count
This script is for functions that return the distribution of leading digits of a numerical distribution.
Make sure you numerical distribution spans a few orders of magnitude.

Author: ayoubft
"""

# Imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

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


def plot_benford(X, B, ff1, ff2, ff3):
    """
    This function is to automate plotting Benford distributions 
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
    
    return 0



X = list(range(1,  10))

B = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]



# Other method: 
#def leadingDigit(x):
#    while x >= 10:
#        x //= 10
#    return x
