import numpy as np
my_arr = np.random.randint(1,101,size=(5,5))
#Original Matrix
print("Original Matrix: \n",my_arr)
# max,min and mean values
print("min value: ",my_arr.min())
print("max value: ",my_arr.max())
print("mean value: ",my_arr.mean())

# Normalize between 0 and 1  --> (x - min) / (max - min)
normalized_arr= (my_arr - my_arr.min()) / (my_arr.max() - my_arr.min())
print("Normalized Matrix: \n",normalized_arr)

# Flatten to 1D array and sort
flattened_arr = normalized_arr.reshape(-1)
sorted_arr = np.sort(flattened_arr)
print("Flattened Matrix: \n",flattened_arr)
print("sorted Matrix: \n",sorted_arr)
