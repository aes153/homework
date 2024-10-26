calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string_low = string.lower()
    return any(string_low in item.lower() for item in list_to_search)

print(string_info('Ястреб'))
print(string_info('Тригонометрия'))
print(string_info('Волшебство'))
print(is_contains('Мак', ['СмАк', 'маЯк', 'МАк']))
print(is_contains('Стол', ['УсТоИ', 'стОЙкА', 'аТОлл']))

print(calls)
