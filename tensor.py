import torch
import numpy as np

# python list 
my_list = [[1, 2, 3, 4, 5] , [5, 10, 8, 7, 9]]
print(my_list)

# numpy array 
np1 = np.random.rand(3, 4)
print(np1)

# get the type of the numpy array 
print(np1.dtype)   # default type is float64

# tensor 
tensor_2d = torch.rand(3, 4)
print(tensor_2d)
print(tensor_2d.type)   # default type is float32

tensor_3d = torch.rand(2, 3, 4)
print(tensor_3d)

# create a tensor out of a numpy aarray
tensor_np = torch.tensor(np1)
print(tensor_np)   # type is float64 
