import matplotlib.pyplot as plt
import time

# Fungsi pembagian titik-titik
def divide_points(points,left_ctrl,right_ctrl):
    if(len(points) > 1):
        new_points = []
        for i in range(len(points) - 1):
            x = (points[i][0] + points[i+1][0]) / 2
            y = (points[i][1] + points[i+1][1]) / 2
            new_points.append((x, y))
        left_ctrl.append(new_points[0])
        right_ctrl.insert(0,new_points[-1])
        return divide_points(new_points,left_ctrl,right_ctrl)
    else:
        return points[0],left_ctrl,right_ctrl

# Fungsi pembentukan kurva Bezier dengan algoritma divide and conquer
def bezier_curve(points, iterations, main_points):
    if(iterations != 0 and len(points) > 1):
        left_ctrl = [points[0]]
        right_ctrl = [points[-1]]
        point, left_ctrl, right_ctrl = divide_points(points, left_ctrl, right_ctrl)
        index = main_points.index(points[0])
        main_points.insert(index+1, point)
        bezier_curve(left_ctrl, iterations-1, main_points)
        bezier_curve(right_ctrl, iterations-1, main_points)


# Fungsi untuk menampilkan plot
def plot_curve_and_points(curve_points, control_points, ax):
    ax.plot([p[0] for p in curve_points], [p[1] for p in curve_points], 'r-', label='Kurva Bezier')
    ax.plot([p[0] for p in control_points], [p[1] for p in control_points], 'bo-', label='Titik-titik kontrol')
    for i in range(len(control_points) - 1):
        ax.plot([control_points[i][0], control_points[i+1][0]], [control_points[i][1], control_points[i+1][1]], 'g--')
    ax.legend()
    # ax.title('Kurva Bezier dan Titik-titik Kontrol')   
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.axis('equal')

def show_curve(control_points, iteration, ax):
    for i in range(1, iteration + 1):
        curve_points = [control_points[0], control_points[-1]]
        ax.cla()
        ax.set_title("Divide and Conquer")
        tstart = time.time()
        bezier_curve(control_points, i, curve_points)
        plot_curve_and_points(curve_points, control_points, ax)
        tend = time.time()
        if i == iteration:
            ax.text(0.5, -0.1, f"Execution Time in {i} iteration : {round(tend - tstart, 5)} seconds", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        
        print(i, " Waktu Eksekusi : ", round(tend - tstart, 5), "s")
        plt.pause(1)



# Contoh penggunaan
# points = [(3,4),(0, 0), (2, 1),(1,3)]
# # points = sortX(points)
# curve_points = [points[0],points[-1]]
# bezier_curve(points, 10,curve_points)
# plot_curve_and_points(curve_points, points)