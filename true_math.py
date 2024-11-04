import math

def true_divide(first, second):
    if second == 0:
        return math.inf
    else:
        return first / second

result3 = true_divide(123, 3)
result4 = true_divide(48, 0)
# print(result3)
# print(result4)