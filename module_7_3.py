class WordsFinder:
    file_names = []

    def __init__(self, *files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.files:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    import string
                    table = str.maketrans("", "", string.punctuation)
                    new_line = line.translate(table)
                    list_of_words = str.split(new_line)
                    all_words[file_name] = list_of_words
                    return all_words

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

# print(finder2.find('TEXT')) # 3 слово по счёту
#
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего