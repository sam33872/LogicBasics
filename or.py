import numpy as np

W = np.array([0.6, 0.6])
b = -0.1

I = [[0, 0], [1, 0], [0, 1], [1, 1]]

O = [2, 2, 2, 2]

def Step(num):
    if num > 0:
        return 1
    else:
        return 0

x = 0
for i in I:
    O[x] = Step(W.dot(i)+b)
    print("Inputs: " + str(i) + " Output: " + str(O[x]))
    x = x + 1
