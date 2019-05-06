#1. Создайте класс Word.
#2. Добавьте свойства text и part of speech.
#3. Добавьте возможность создавать объект слово со значениями в скобках.
#4. Создайте класс Sentence
#5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
#6. Добавьте метод show, составляющий предложение.
#7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

class Word:
    text = ''
    part_of_speech = ''

    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech



class Sentence:
    content = [4,2,3,1]
    text = []
    part_of_speech = []
    index = 0
    words = []




    def __init__(self, text, part_of_speech, index):
        self.text = text
        self.part_of_speech = part_of_speech
        self.index = index



    def show(self, indexs, content):
        self.indexs = indexs
        self.content = content
        for n in self.content:
            if self.indexs != n:
                self.index = n




word1 = Word ('программист', 'существительное')
word2 = Word ('программа','существительное')
word3 = Word ('программировать', 'глагол')



word4 = Sentence ('программист', 'существительное', 1)
word5 = Sentence ('написал', 'глагол',2)
word6 = Sentence ('программу','существительное', 3)
word7 = Sentence ('вчера', 'местоимение', 4)


#words =  ('программист', 'написал', 'программу','вчера')



