        print("left_points: ")
        print(left_points)
        print("right_points: ")
        print(right_points)
        return left_points[:-1] + divide_points([left_points[-1], right_points[0]]) + right_points
