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
def plot_bezier_curve(control_points, iteration, ax):
    tot_point = 2 ** iteration + 1
    t_values = np.linspace(0, 1, tot_point)
    curve_points = np.array([bf(control_points, t) for t in t_values])

    ax.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    ax.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bezier Curve')
    ax.grid(True)
    ax.axis('equal')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()




def show_curve(control_points_coord, iteration, ax):
    control_points = np.array(control_points_coord, dtype=np.float64)
    for i in range(1, iteration+1):
        ax.cla()
        ax.set_title("Brute Force")
        tstart = time.time()
        plot_bezier_curve(control_points, i, ax)
        tend = time.time()
        if i == iteration:
            ax.text(0.5, -0.1, f"Execution Time in {i} iterations: {round(tend - tstart, 5)} seconds", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        
        print(i, " Waktu Eksekusi : ", round(tend - tstart,5), " s")
        plt.pause(1)
    
 

