import matplotlib.pyplot as plt
import numpy as np

# Membuat kurva bezier dengan menggunakan algoritma devide and conquer
def devide_and_conquer(points: list,left_ctrl :list, right_ctrl : list,n : int) -> tuple:
    print(f"left_ctrl: {left_ctrl}")
    print(f"right_ctrl: {right_ctrl}")
    if(len(points) > 1):
        new_array = []
        for i in range(len(points)-1):
            x = (points[i][0] + points[i+1][0])/(n-1)
            y = (points[i][1] + points[i+1][1])/(n-1)
            new_array.append((x, y))
            if(i == 0):
                left_ctrl.append((x, y))
            if(i == len(points)-2):
                right_ctrl.append((x, y))
            return devide_and_conquer(new_array,left_ctrl,right_ctrl,n)
    else:
        left_ctrl.append(points[0])
        right_ctrl.append(points[0])
        return points[0],left_ctrl, right_ctrl


def bezier_curve_n(points: list, iter:int, ctrl_points: list):
    print(ctrl_points)
    print(points)
    # sorting list berdasarkan x
    points = sorted(points, key=lambda x: x[0])
    n = len(points)
    if(n<3):
        print("Minimum 3 points required")
        return
    elif(iter>0):
        point,left_ctrl,right_ctrl = devide_and_conquer(points,[],[],n)
        # print(len(left_ctrl))
        # print(len(right_ctrl))
        iter -=1
        ctrl_points.append(point)
        left = bezier_curve_n(left_ctrl,iter,ctrl_points)
        right = bezier_curve_n(right_ctrl,iter,ctrl_points)
        return list(set(left) | set(right))
    else:
        return ctrl_points

import matplotlib.pyplot as plt

# Membuat fungsi untuk menampilkan plot
def plot_curve_and_points(curve_points, points):
    # Plot kurva Bezier
    plt.plot([p[0] for p in curve_points], [p[1] for p in curve_points], 'r-', label='Kurva Bezier')
    # Plot titik-titik kontrol
    plt.plot([p[0] for p in points], [p[1] for p in points], 'bo-', label='Titik-titik kontrol')
    # Plot garis yang menghubungkan titik-titik kontrol
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], 'g--')
    plt.legend()
    plt.title('Kurva Bezier dan Titik-titik Kontrol')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

points = [(0, 0), (1, 1), (2, 2), (3, 3)]
ctrl_points = [(0,0),(3,3)]

bezer_curve = bezier_curve_n(points, 3, ctrl_points)
# Contoh penggunaan
plot_curve_and_points(bezer_curve, points)


