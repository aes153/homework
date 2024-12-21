first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(f) for f in first_strings if len(f) > 5]
print(first_result)

second_result = [(f,s) for f in first_strings for s in second_strings if len(f) == len(s)]
print(second_result)

third_result = {t: len(t) for t in first_strings + second_strings if len(t)%2 == 0}
print(third_result)