import numpy as np

# arr_2d=np.array([1,2,3,4,5,6])
# new_2d_arr=np.insert(arr_2d,2,7,axis=0)
# print(new_2d_arr)

arr_2d=np.array([[1,2],[3,4],[5,6]])
new_2d_arr=np.insert(arr_2d,2,[8,9],axis=0)
print(new_2d_arr)