import sys
sys.path.append('../src')

import BruteBezier
import DNCBezierN


import matplotlib.pyplot as plt
import time

def input_tuples():
    tuples = []
    print("Enter coord (x,y) (Press Enter to stop): ")
    while True:
        try:
            nums = input(">> ").split()
            if not nums:
                break
            if len(nums) != 2:
                raise ValueError("Invalid input.")
            tuples.append([int(num) for num in nums])
        except ValueError as e:
            print(f"Invalid input: {e}")
    return tuples

def show_curves(control_points, iter):
    array_of_tuples = [(x, y) for x, y in control_points]
    fig, axs = plt.subplots(1, 2,figsize = (12.5,6.2)) 
    fig.suptitle('Bezier Curves Comparison') 
    print("===========DivideNConquer=============")
    DNCBezierN.show_curve(array_of_tuples, iter, axs[0])
    axs[0].set_title('Divide and Conquer')
    print("===========BruteForce=============")
    BruteBezier.show_curve(control_points, iter, axs[1])
    axs[1].set_title('Brute Force')

    plt.show()


control_points = input_tuples()
iter = int(input("How many iterations? : "))
show_curves(control_points, iter)
