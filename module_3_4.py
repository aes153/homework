def single_root_words(root_word, *other_words):
    same_words = []
    root_word_low = root_word.lower()

    for i in other_words:
        i_low = i.lower()
        if (i_low in root_word_low or
            root_word_low in i_low):
            same_words.append(i)
    return same_words


result1 = single_root_words('Стол', 'ПреСтол', 'стоЯнкА', 'ПроСтотА', 'Столица')
result2 = single_root_words('дракон', 'рак', 'ДраКа', 'кОн', 'дРагоценнОсть')
print(result1)
print(result2)

