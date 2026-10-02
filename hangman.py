import random
import tkinter as tk

MAX_MISTAKES = 6
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
    r"""
       +---+
           |
           |
           |
           |
    =========""",
    r"""
       +---+
       O   |
           |
           |
           |
    =========""",
    r"""
       +---+
       O   |
       |   |
           |
           |
    =========""",
    r"""
       +---+
       O   |
      /|   |
           |
           |
    =========""",
    r"""
       +---+
       O   |
      /|\\  |
           |
           |
    =========""",
    r"""
       +---+
       O   |
      /|\\  |
      /    |
           |
    =========""",
    r"""
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
        return self.mistakes >= MAX_MISTAKES
    def wrong_letters(self):
        ## цикл для проверки
        result = []
        for l in self.guessed:
            if l not in self.word:
                result.append(l)
        return sorted(result)

def play_gui():
    root = tk.Tk()
    root.title("Висельница")
    root.geometry("600x600")
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

    guessed_label = tk.Label(root, text = f"Неправильные буквы: {game.wrong_letters()}", font = ("Arial", 14))
    guessed_label.pack(pady = 5)

    entry = tk.Entry(root, font = ("Arial", 18), width = 5, justify = "center")
    entry.pack(pady = 10)

    def new_game():
        nonlocal game, word
        word = random.choice(WORDS)
        game = Game(word)
        word_label.config(text = game.display_word())
        pic_label.config(text = HANGMAN_PICS[game.mistakes])
        err_label.config(text = f"Ошибки: ({game.mistakes}/{MAX_MISTAKES})")
        all_guessed = " ".join(sorted(game.guessed))
        guessed_label.config(text = f"Неправильные буквы: {all_guessed}")
        entry.delete(0, tk.END)
        entry.focus()

    def on_guess():
        letter = entry.get().strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            return
        game.guess(letter)
        word_label.config(text = game.display_word())
        pic_label.config(text = HANGMAN_PICS[game.mistakes])
        err_label.config(text = f"Ошибки: ({game.mistakes}/{MAX_MISTAKES})")
        all_guessed = " ".join(sorted(game.guessed))
        guessed_label.config(text = f"Неправильные буквы: {all_guessed}")
        entry.delete(0, tk.END)
        if game.is_won():
            word_label.config(text = f"Слово угадано! Слово: {game.word}")
        elif game.is_lost():
            word_label.config(text = f"Вы проиграли. Слово было: {game.word}")

    btn = tk.Button(root, text = "Угадать", font = ("Arial", 14), width = 10, command = on_guess)
    btn.pack(pady = 10)

    btn_new = tk.Button(root, text = "Новая игра", font = ("Arial", 14), width = 10, command = new_game)
    btn_new.pack(pady = 10)
    
    root.mainloop()
play_gui()