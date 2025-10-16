import numpy as np

# temperature=np.array([30.5,32.0,28.4,25.2,25.8,29.0,27.5])
# print("mean temperature :",np.mean(temperature))

# zeroes_array=np.zeros(3)
# print(zeroes_array)

# onees_array=np.ones((2,3))
# print(onees_array)

# filled_array=np.full((2,2),7)
# print(filled_array)

arr=np.arange(1,10,2)
print(arr)

# identity_matrix=np.eye(3)
# print(identity_matrix)

# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# # print(arr.shape)
# # print(arr.size)
# # print(arr.ndim)
# # print(arr.dtype)
# arr1=arr.astype(np.float64)
# print(arr1)
# print(arr1.dtype)

arr=np.array([1,2,3,4,5,6])
rshaped_arr=arr.reshape(2,3)
print(rshaped_arr)
arr1=rshaped_arr.ravel()
print(arr1)