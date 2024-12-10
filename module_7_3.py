import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = string.punctuation.replace('-', '')

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for char in punctuation:
                    content = content.replace(char, '')
                    words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        found_positions = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            index = words.index(word)
            found_positions[file_name] = index + 1
        return found_positions

    def count(self, word):
        counts = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word)
        return counts

file_name1 = 'test_file1.txt'
with open(file_name1, 'w', encoding='utf-8') as f:
    f.write("it's a text for task Найти везде,\n"
             "Используйте его для самопроверки.\n"
             "Успехов в решении задачи!\n"
             "text text text")

finder = WordsFinder(file_name1)
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))


file_name2 = 'Mother Goose.txt'
with open(file_name2, 'w', encoding='utf-8') as f:
    f.write('Monday’s Child\n'
            '\n'
            'Monday’s child is fair of face\n'
            'Tuesday’s child is full of grace\n'
            'Wednesday’s child is full of woe\n'
            'Thursday’s child has far to go,\n'
            'Friday’s child is loving and giving,\n'
            'Saturday’s child works hard for a living\n'
            'And the child that is born on the Sabbath day\n'
            'Is bonny and blithe, and good and gay.\n'
            '\n'
            'Mother Goose')

finder = WordsFinder(file_name2)
print(finder.get_all_words())
print(finder.find('child'))
print(finder.count('child'))