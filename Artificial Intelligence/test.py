import numpy as np

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Paul", "Lesley"]

x = zip(a, b.reshape(5,1))

print(list(x))