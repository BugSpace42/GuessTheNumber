import tkinter as tk

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай число")
        self.root.geometry("400x300")

        # Переменные игры
        self.secret_number = None
        self.attempts_left = 0
        self.difficulty = None
        self.attempts_made = 0

        # Настройка интерфейса
        self.setup_ui()

    def setup_ui(self):
        # Интерфейс
        pass

    def new_game(self):
        # Новая игра
        pass

    def check_guess(self):
        # Проверка предположения
        pass


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessGame(root)
    root.mainloop()