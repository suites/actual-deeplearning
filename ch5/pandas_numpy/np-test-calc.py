import numpy as np

v = np.zeros(10, dtype=np.float32)
print(v)

v = np.arange(10, dtype=np.uint64)
print(v)

v *= 3
print(v)

print(v.mean())