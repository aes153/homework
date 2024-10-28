def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [(9, 8, 7), 'string', False]
values_list_2 = [3.14, 'circle']

print_params()
print_params(b = 25, c = [1, 2, 3])
print_params(*values_list)
print_params(*values_list_2, 748)

def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
values_dict = {'a': 95, 'b': 'my_string', 'c': False}
print_params(**values_dict)
