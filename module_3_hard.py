def calculate_structure_sum(*args):
    sum = 0

    for arg in args:
        if isinstance(arg, int):
            sum += arg
        elif isinstance(arg, str):
            sum += len(arg)
        elif isinstance(arg, (list, set, tuple)):
            sum += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):  # Словарь
            for key, value in arg.items():
                sum += calculate_structure_sum(key, value)
    return sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(*data_structure)
print(result)