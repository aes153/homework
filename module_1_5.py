immutable_var = 15, 'october', 3, 8, 'python'
print(immutable_var)
immutable_var[1] = 'tea'
print(immutable_var
# Кортеж является неизменяемой переменной, поэтому программа не поддерживает назначение элементов
mutable_var = [True, 'horse', 77, 'sky']
print(mutable_var)
mutable_var[0:2] = False, 'cat'
print(mutable_var)