import BruteBezier
def input_tuples():
    tuples = []
    while True:
        try:
            nums = input("Enter coord (x,y) (Enter saja untuk stop): ").split()
            if not nums:
                break
            if len(nums) != 2:
                raise ValueError("Tidak valid.")
            tuples.append([int(num) for num in nums])
        except ValueError as e:
            print(f"Invalid input: {e}")
    return tuples


tuples =  input_tuples()
iter = int(input("Berapa iterasi? : "))
BruteBezier.show_curve(tuples,iter)
