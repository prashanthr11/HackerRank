import numpy as np

l = list(map(int, input().split()))
n = np.array(l)
print(np.reshape(n, (3, 3)))
