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
        self.title_label = tk.Label(
            self.root,
            text="Угадай число",
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=10)

        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack(pady=20)

        tk.Label(self.difficulty_frame, text="Выберите сложность:").pack()

        self.difficulty_var = tk.StringVar(value="medium")
        difficulties = [("Легкий", "easy"), ("Средний", "medium"), ("Сложный", "hard")]

        for text, value in difficulties:
            tk.Radiobutton(
                self.difficulty_frame,
                text=text,
                variable=self.difficulty_var,
                value=value
            ).pack()

        self.start_button = tk.Button(
            self.root,
            text="Начать игру",
            command=self.new_game,
            bg="green",
            fg="white",
            font=("Arial", 12)
        )
        self.start_button.pack(pady=10)

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