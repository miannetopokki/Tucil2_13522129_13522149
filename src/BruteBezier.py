import numpy as np
import matplotlib.pyplot as plt
import time




import numpy as np
import matplotlib.pyplot as plt


        
def bf(control_points, t):
    n = len(control_points) - 1

    if n == 1:
        return (1 - t) * control_points[0] + t * control_points[1]

    points = [(1 - t) * control_points[i] + t * control_points[i + 1] for i in range(n)]
    left_curve = bf(points, t)
    right_curve = bf(points, t)
    
    result = (1 - t) * left_curve + t * right_curve
    return result

def plot_bezier_curve(control_points, iteration):
    if(iteration == 1):
        tot_point = 3
    else:
        tot_point = iteration ** 2 + 1
    t_values = np.linspace(0, 1, tot_point)
    curve_points = np.array([bf(control_points, t) for t in t_values])

   
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bezier Curve')


    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()



def show_curve(control_points_coord,iteration):
    control_points = np.array(control_points_coord, dtype=np.float64)
    plt.figure()
    for i in range(1,iteration+1):
        plt.cla()
        plt.title(i)
        plot_bezier_curve(control_points,i)
        plt.pause(1)
    
    plt.show()

