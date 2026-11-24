import torch
import numpy as np


tensor_a = torch.tensor([1, 2, 3, 4])
tensor_b = torch.tensor([5, 6, 7, 8])

# short hand addition 
print(tensor_a + tensor_b)

# long hand addition 
print(torch.add(tensor_b, tensor_a))

# substract 
print(tensor_b - tensor_a)

# sub function 
print(torch.sub(tensor_b, tensor_a))

# multiplication 
print(tensor_b * tensor_a)

# function 
print(torch.mul(tensor_a, tensor_b))

# divison 
print(tensor_b / tensor_a) # converst it into a float

# function 
print(torch.div(tensor_b , tensor_a))

# remainders
print(tensor_b % tensor_a) # a list of remainders


# long hand 
print(torch.remainder(tensor_b , tensor_a))

# exponents / power
print(torch.pow(tensor_a, tensor_b))

# another way to write an opperation
print(tensor_a.add(tensor_b))


# reasignement 
# instead of doing tensor_a = tensor_a + tensor_b
tensor_a.add(tensor_b)
print(tensor_a)