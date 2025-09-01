import numpy as np

my_arr = np.random.randint(1,101,size=(5,5))
print("Original matrix: \n",my_arr)

sliced_arr = my_arr[1:4,1:4]
print("Sliced 3x3 Matrix: \n",sliced_arr)