import random
import sys
import tkinter as tk
from colorama import Fore, Style, init

max_mistake = 6
WORDS = [
    "питон",
    "программирование",
    "алгоритм",
    "переменная",
    "функция",
    "цикл",
    "массив",
    "компьютер",
    "клавиатура",
    "монитор",
    "интернет",
    "программа",
    "разработка",
    "ошибка",
    "код",
]
HANGMAN_PICS = [
    """
       +---+
           |
           |
           |
           |
    =========""",
    """
       +---+
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

class Game:
    def __init__ (self, word):
        ## создание массива и слова
        self.word = word.lower()
        self.guessed = set()
        self.mistakes = 0
    def display_word (self):
        ## Проверка на то есть ли буква
        result=[]
        for letter in self.word:
            if letter in self.guessed:
                result.append(letter.upper())
            else:
                result.append("_")
        return " ".join(result)
    def guess (self, letter):
        ## вывод результата букв, добавление в массив буквы
        letter = letter.lower()
        if letter in self.guessed:
            return "already"
        self.guessed.add(letter)
        if letter in self.word:
            return "correct"
        else:
            self.mistakes += 1
            return "wrong"
    def is_won (self):
        ## победил ли игрок, если слова нет в массиве то нет
        for letter in self.word:
            if letter not in self.guessed:
                return False
        return True
    def is_lost(self):
        ## проиграл ли игрок
        return self.mistakes >= max_mistake
    def wrong_letter(self):
        ## цикл для проверки
        result = []
        for l in self.guessed:
            if l not in self.word:
                result.append(l)
        return sorted(result)

##    word = random.choice(WORDS)
##    game = Game(word)
##    while not game.is_won() and not game.is_lost():
##        print (HANGMAN_PICS[game.mistakes])
##        print("Слово: ", game.display_word())
##        print("Ошибки: ", game.wrong_letter(), f"({game.mistakes}/{max_mistake})")
##        while True:
##            letter = input("Слово: ").strip().lower()
##            if len(letter) == 1 and letter.isalpha():
##                break
##            print("Нужна ровно 1 буква!")
##        result = game.guess(letter)
##        if result == "correct":
##            print("Буква добавлена")
##        elif result == "wrong":
##            print("Нет такой буквы")
##        elif result == "already":
##            print("Уже есть такая буква")
##    print(HANGMAN_PICS[game.mistakes])
##    if game.is_won():
##        print("Слово угадано! Слово: ", word)
##        print("Количество ошибок: ", game.mistakes)
##        print("Неправильные буквы: ", game.wrong_letter())
##    elif game.is_lost():
##        print("Вы проиграли. Слово было: ", word)
##        print("Количество ошибок: ", game.mistakes)
##        print("Неправильные буквы: ", game.wrong_letter())
##        print("Ваш результат: ", game.display_word())

##play()
def play_gui():
    root = tk.Tk()
    root.title("Висельница")
    root.geometry("500x700")
    word = random.choice(WORDS)
    game = Game(word)

    title_label = tk.Label(root, text = "Висельница", font = ("Arial", 24, "bold"))
    title_label.pack(pady = 10)

    pic_label = tk.Label(root, text = HANGMAN_PICS[0], font = ("Courier", 14))
    pic_label.pack(pady = 10) 

    word_label = tk.Label(root, text = game.display_word(), font = ("Arial", 24))
    word_label.pack(pady = 10)

    err_label = tk.Label(root, text = "Ошибки: (0/6)", font = ("Arial", 14))
    err_label.pack(pady = 10)

    entry = tk.Entry(root, font = ("Arial", 18), width = 5, justify = "center")
    entry.pack(pady = 10)

    btn = tk.Button(root, text = "Угадать", font = ("Arial", 14), width = 10)
    btn.pack(pady = 10)
    root.mainloop()
play_gui()