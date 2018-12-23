import numpy as np

# 3D : depth * row * column

d = np.array([[[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],

               [[13,14,15,16],
                [17,18,19,20],
                [21,22,23,24]]])
print(d)
print(d.ndim)       # rank : 3
print(d.shape)      # (2,3,4) : 2 depth * 3 rows * 4 columns
print(len(d))       # depth : 2
print(len(d[0]))    # row : 3
print(len(d[0][0])) # column : 4
