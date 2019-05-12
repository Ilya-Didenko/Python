#1. Создайте класс Word.
#2. Добавьте свойства text и part of speech.
#3. Добавьте возможность создавать объект слово со значениями в скобках.
#4. Создайте класс Sentence
#5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
#6. Добавьте метод show, составляющий предложение.
#7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

class Word:

    def __init__(self, text = '', part_of_speech = ''):
        self.text = text
        self.part_of_speech = part_of_speech

class Sentence:

# можно не задавать пустые значения списков, но тогда обязателен ввод данных, иначе ошибка.
    def __init__(self, content=[], list=[]):
        self.content = content
        self.list = list

    def show(self):
        result = [self.list[i].text for i in self.content]
 # выводим результат строкой, разделение пробелами, с заглавной буквы
        result_2 = ' '.join(result).capitalize()
        return result_2

    def show_parts(self):
        result = [self.list[i].part_of_speech for i in self.content]
# переводим результат в множество (удаляем повторения)
        result = set(result)
        result_3 = 'Части речи, входящие в предложение: %s.' % ', '.join(result)
        return result_3

in_sentence = Sentence([3, 0, 2, 1], [Word('программист', 'существительное'), Word('написал', 'глагол'),
                                      Word('программу', 'существительное'), Word('вчера', 'наречие')])
print(in_sentence.show())
print(in_sentence.show_parts())