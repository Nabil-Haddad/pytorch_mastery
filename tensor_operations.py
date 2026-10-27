import torch

my_torch = torch.arange(10)
print(my_torch)

# reshape and View
my_torch = my_torch.reshape(2, 5)
print(my_torch)


# his will cause an error
# my_torch = my_torch.reshape(2, 5)
# print(my_torch)

# reshape if we don't know the number of items using -1
my_torch2 = torch.arange(10)
my_torch2 = my_torch2.reshape(2 , -1)

# there are differences between reshape and view
my_torch3 = torch.arange(10)
print(my_torch3)

my_torch4 = my_torch3.view(2, 5)
print(my_torch4)



# tensors with reshape and view will be also updated
# Reshape
my_torch5 = torch.arange(10)
print(my_torch5)

my_torch6 = my_torch5.reshape(2,5)
print(my_torch6)

# modifying 
my_torch5[1] = 250
print(my_torch5)
print(my_torch6)


# view
my_torch7 = torch.arange(10)
print(my_torch7)

my_torch8 = my_torch5.view(2,5)
print(my_torch8)

# modifying 
my_torch7[1] = 5326
print(my_torch7)
print(my_torch8)

# grab a specific item
print(my_torch7[2]) # grabs a tensor not a number

# grab a slice
my_torch9 = my_torch7.reshape(5,2)
print(my_torch9[:1])

# keep the shape
print(my_torch9[:,1:])