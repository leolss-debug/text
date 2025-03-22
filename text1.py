import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
c = slice( 0,2)

print(a[0][0])
print(a[0][0:])
print(a[c])