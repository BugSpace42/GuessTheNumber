import tkinter as tk
from tkinter import messagebox, ttk
import random

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
            command=self.start_game,
            bg="green",
            fg="white",
            font=("Arial", 12)
        )
        self.start_button.pack(pady=10)

    def show_game_interface(self):
        self.difficulty_frame.pack_forget()
        self.start_button.pack_forget()

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=20)

        self.info_label = tk.Label(
            self.game_frame,
            text=f"Загадано число {self.range_text}",
            font=("Arial", 12)
        )
        self.info_label.pack()

        self.attempts_label = tk.Label(
            self.game_frame,
            text=f"Осталось попыток: {self.attempts_left}",
            font=("Arial", 10)
        )
        self.attempts_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.game_frame, width=15, font=("Arial", 14))
        self.guess_entry.pack(pady=10)
        self.guess_entry.focus()

        self.check_button = tk.Button(
            self.game_frame,
            text="Проверить",
            command=self.check_guess,
            bg="blue",
            fg="white",
            font=("Arial", 12)
        )
        self.check_button.pack(pady=5)

        self.message_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 10),
            wraplength=350
        )
        self.message_label.pack(pady=10)

        self.new_game_button = tk.Button(
            self.game_frame,
            text="Новая игра",
            command=self.reset_to_menu,
            bg="orange",
            font=("Arial", 10)
        )
        self.new_game_button.pack(pady=5)

        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

    def start_game(self):
        self.difficulty = self.difficulty_var.get()

        if self.difficulty == "easy":
            self.secret_number = random.randint(1, 100)
            self.attempts_left = 20
            self.range_text = "от 1 до 100"
        elif self.difficulty == "medium":
            self.secret_number = random.randint(1, 100)
            self.attempts_left = 15
            self.range_text = "от 1 до 100"
        else:
            self.secret_number = random.randint(1, 100)
            self.attempts_left = 10
            self.range_text = "от 1 до 100"

        self.attempts_made = 0
        self.show_game_interface()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.message_label.config(text="Пожалуйста, введите число!")
            return

        self.guess_entry.delete(0, tk.END)
        self.attempts_left -= 1
        self.attempts_made += 1

        if guess == self.secret_number:
            self.show_win_message()
            return

        if self.attempts_left == 0:
            self.show_lose_message()
            return

        if guess < self.secret_number:
            hint = "Загаданное число больше"
        else:
            hint = "Загаданное число меньше"

        self.message_label.config(
            text=f"{hint}\nОсталось попыток: {self.attempts_left}"
        )
        self.attempts_label.config(
            text=f"Осталось попыток: {self.attempts_left}"
        )

    def show_win_message(self):
        result = messagebox.askyesno(
            "Победа!",
            f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts_made} попыток!\n"
            "Хотите сыграть еще?"
        )
        if result:
            self.reset_to_menu()
        else:
            self.root.quit()

    def show_lose_message(self):
        result = messagebox.askyesno(
            "Поражение",
            f"Ваши попытки закончились. Загаданное число: {self.secret_number}\n"
            "Хотите попробовать еще?"
        )
        if result:
            self.reset_to_menu()
        else:
            self.root.quit()

    def reset_to_menu(self):
        self.game_frame.destroy()
        self.difficulty_frame.pack()
        self.start_button.pack()

        self.secret_number = None
        self.attempts_left = 0
        self.attempts_made = 0


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessGame(root)
    root.mainloop()