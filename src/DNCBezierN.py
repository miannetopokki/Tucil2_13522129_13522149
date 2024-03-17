import matplotlib.pyplot as plt

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
        return left_ctrl,right_ctrl

# Fungsi pembentukan kurva Bezier dengan algoritma divide and conquer
def bezier_curve(points, iterations):
    if iterations == 0 or len(points) < 2:
        return points
    else:
        left_ctrl = [points[0]]
        right_ctrl = [points[-1]]
        left_ctrl, right_ctrl = divide_points(points, left_ctrl, right_ctrl)
        return bezier_curve(left_ctrl, iterations - 1) + bezier_curve(right_ctrl, iterations - 1)


# Fungsi untuk menampilkan plot
def plot_curve_and_points(curve_points, control_points):
    plt.plot([p[0] for p in curve_points], [p[1] for p in curve_points], 'r-', label='Kurva Bezier')
    plt.plot([p[0] for p in control_points], [p[1] for p in control_points], 'bo-', label='Titik-titik kontrol')
    for i in range(len(control_points) - 1):
        plt.plot([control_points[i][0], control_points[i+1][0]], [control_points[i][1], control_points[i+1][1]], 'g--')
    plt.legend()
    plt.title('Kurva Bezier dan Titik-titik Kontrol')   
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Contoh penggunaan
points = [(0, 0), (1, 2), (3, 1), (4, 3)]
curve_points = bezier_curve(points, 5)
# print(curve_points)
plot_curve_and_points(curve_points, points)
