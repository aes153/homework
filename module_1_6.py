my_dict = {'Anna': 1990, 'Boris': 1991, 'Stas': 1992}
print(my_dict)
print(my_dict['Boris'])
my_dict['Robert'] = 1995
print(my_dict)
my_dict.update({'Vlad': 1993, 'Maria': 1994})
print(my_dict)
my_dict.pop('Maria')
print(my_dict)

my_set = {1,'f', 1, 5, 'l', 1, 8,'f'}
print(my_set)
my_set.add(3)
my_set.add(10)
my_set.discard('f')
print(my_set)