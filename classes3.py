# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.

class Word:
    def __init__(self, text='', part_of_speech='', grammatical_characteristics=''):

        self.text = text
        self.part_of_speech = part_of_speech
        self.__grammatical_characteristics = grammatical_characteristics

    def get_params(self):
        return self.__grammatical_characteristics

class Noun(Word):
    def __init__(self, text, grammatical_characteristics='', part_of_speech='существительное'):
# super - указывает, что параметры беруться из Word (можно указывать Word. ....)
        super().__init__(text, part_of_speech, grammatical_characteristics)

class Verb(Word):
    def __init__(self, text, grammatical_characteristics='', part_of_speech='глагол'):
        super().__init__(text, part_of_speech, grammatical_characteristics)

class Sentence:
    def __init__(self, content=[], list=[]):
        self.content = content
        self.list = list

    def show(self):
        result = [self.list[i].text for i in self.content]
        result2 = ' '.join(result).capitalize()
        return result2

    def show_parts(self):
        result3 = []
        for i in self.content:
            result_parts = self.list[i].get_params().split(', ')
            for e in result_parts:
                result3.append(e)

        result = set( result3)
        sresult4 = 'Грамматические характеристики: %s.' % ', '.join(result)
        return sresult4

in_sentence = Sentence([0, 2, 1], [Noun('программист', 'мужской род, единственное число, иминительный падеж'),
                                      Verb('написал', 'единственное число, прошедшие время,'),
                                      Noun('программу', 'женский род, единственное число, винительный падеж')])

print(in_sentence.show_parts())
