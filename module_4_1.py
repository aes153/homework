from fake_math import fake_divide as fd, result1, result2
from true_math import true_divide as td, result3, result4

result1 = fd(18, 6)
result2 = fd(125, 0)
result3 = td(196, 14)
result4 = td(987, 0)

print(result1)
print(result2)
print(result3)
print(result4)