import numpy as np
import matplotlib.pyplot as plt
import time




import numpy as np
import matplotlib.pyplot as plt


def get_mid(x1, x2, y1, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2





def dnc(control_points, iteration):
    tempMid = []
    curveCord = []

    for j in range(len(control_points) - 1):
        posX = (control_points[j][0] + control_points[j+1][0]) / 2
        posY = (control_points[j][1] + control_points[j+1][1]) / 2
        tempMid.append([posX, posY])

    curveCord.append(control_points[0])  
    for i in range(iteration):
        newMid = []
        newMid.append(control_points[0])
        newMid.extend(tempMid) 
        newMid.append(control_points[-1])
        for j in range(len(newMid) - 1):
            X = (newMid[j][0] + newMid[j+1][0]) / 2
            Y = (newMid[j][1] + newMid[j+1][1]) / 2
            curveCord.append([X, Y])
    curveCord.append(control_points[-1])  
    Dots = np.array(curveCord, dtype=np.float64)
    print(curveCord)

    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(Dots[:, 0], Dots[:, 1], 'b-', label='Bezier Curve')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()



def dncRek(control_points, iteration, current_iteration, curve):
    if current_iteration < iteration:
        x1, y1 = get_mid(control_points[0][0], control_points[1][0], control_points[0][1], control_points[1][1])
        x2, y2 = get_mid(control_points[1][0], control_points[2][0], control_points[1][1], control_points[2][1])
        x3, y3 = get_mid(x1, x2, y1, y2)

        current_iteration += 1
        new_temp = [[control_points[0][0], control_points[0][1]], [x1, y1], [x3, y3]]
        dncRek(new_temp, iteration, current_iteration, curve)
        curve.append([x3, y3])

        new_temp2 = [[x3, y3], [x2, y2], [control_points[2][0], control_points[2][1]]]
        dncRek(new_temp2, iteration, current_iteration, curve)

control_points = np.array([[1, 1], [-4, 3], [9, 4]],dtype=np.float64)
curve = [[control_points[0][0],control_points[0][1]]]

dncRek(control_points, 2, 0, curve)
curve.append([control_points[2][0],control_points[2][1]])
curveAddr = np.array(curve, dtype=np.float64)
print(curve)
plt.figure()
plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
plt.plot(curveAddr[:, 0], curveAddr[:, 1], 'b-', label='Bezier Curve')


plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
