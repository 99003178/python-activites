
       class Hangman:
    def __init__(self):
        self.words = {
                      'beach': 'Somewhere near an ocean',
                      'jerky': 'A dried piece of meat',
                      'space': 'The last frontier', 'clouds': 'in the sky',
                      'house': 'A building you spend alot of time in',
                      'trial': 'Something you go though for commiting a crime',
                      'Earth': 'Big, Blue, and green',
                      'money': 'Somthing everyone wants more of',
                      'about': 'close to or almost',
                     }
        for self.word in self.words.keys():
            self.final_word = self.word
            # print(self.final_word)
            break
        self.b = self.words.get('{}'.format(self.final_word))
        self.char_num = 0
        self.word = self.final_word[self.char_num]

    def main(self):
        self.lost = True
        self.amount_found_word = ''
        print("Welcome to guess game\n")
        print("YES")
        hint = input('Would you like a hint?(y/n):')
        if hint == 'y':
            print(self.b)
        for i in range(30):
            self.input_ = input(">>>{}".format(self.amount_found_word))
            try:
                if self.input_ == self.word:
                    self.char_num += 1
                    self.word = self.final_word[self.char_num]
                    self.amount_found_word += self.input_
                    self.input_ += self.word
                if self.input_ == self.final_word:
                    raise IndexError
            except IndexError:
                self.lost = False
                break
        if self.lost:
            print('You Lost...')
        else:
            print('You Won!!! Final Word:{}'.format(self.final_word))

while True:
    hangman = Hangman()
    hangman.main()
    restart = input('Again?(y/n):')
    if restart != 'y':
        break


class prt:
    def func(self):
        print("class inside class")
object = temp object.main
