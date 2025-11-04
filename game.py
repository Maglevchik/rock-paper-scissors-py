import random
import sys
import os

# Словарь допустимых ходов для удобства проверки

class ScoreBoard:
    """Класс для управления счетом и сохранения результатов."""
    CHOICES = {
        "r": "Камень",
        "p": "Бумага",
        "s": "Ножницы"
    }

    FILENAME = "scoreboard.txt"

    def __init__(self):
        # Инициализация счетчиков
        self.user_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self._load_scores() # Загрузка счета при старте

    def _load_scores(self):
        """Загружает счет из файла."""
        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'r') as f:
                try:
                    data = f.read().split(',')
                    self.user_wins = int(data[0])
                    self.computer_wins = int(data[1])
                    self.ties = int(data[2])
                except (ValueError, IndexError):
                    # Игнорировать, если файл поврежден
                    pass

    def _save_scores(self):
        """Сохраняет текущий счет в файл."""
        with open(self.FILENAME, 'w') as f:
            f.write(f"{self.user_wins},{self.computer_wins},{self.ties}")

    def update_score(self, winner):
        """Обновляет счет и сохраняет его."""
        if winner == "user":
            self.user_wins += 1
        elif winner == "computer":
            self.computer_wins += 1
        else:
            self.ties += 1
        self._save_scores()

    def get_user_choice(self):  # <-- Эта функция должна быть здесь
        """
        Получает ход пользователя.
        Отображает доступные клавиши, проверяет ввод и обрабатывает выход из игры.
        """
        while True:
            # Отображение доступных ходов для пользователя
            print("\nСделайте свой ход:")
            print("  (r) - Камень")
            print("  (p) - Бумага")
            print("  (s) - Ножницы")
            print("  (q) - Выход из игры")

            user_input = input("Ваш выбор: ").lower().strip()

            if user_input == 'q':
                # Обработка выхода из игры
                print("Спасибо за игру! До свидания.")
                sys.exit()  # Завершение программы

            if user_input in self.CHOICES:
                return user_input  # Возвращаем корректный ход
            else:
                # Обработка некорректного ввода
                print("🛑 Некорректный ввод. Пожалуйста, выберите r, p, s или q.")

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))

    def determine_winner(self, user_choice, computer_choice):
        if user_choice > computer_choice:
            return "user"
        elif computer_choice > user_choice:
            return "computer"
        elif user_choice == computer_choice:
            return "non wins"

    def display_score(self):
        """Отображает текущий счет."""
        print("\n=== ТЕКУЩИЙ СЧЕТ (С начала) ===")
        print(f"Ваши победы: {self.user_wins}")
        print(f"Победы компьютера: {self.computer_wins}")
        print(f"Ничьи: {self.ties}")
        print("=================================")


def main_game_loop():
    """Основной цикл игры."""
    print("🎉 Добро пожаловать в игру 'Камень-Ножницы-Бумага'! 🎉")

    # Создание экземпляра ScoreBoard
    scoreboard = ScoreBoard() 
    scoreboard.display_score() # Отображение счета при старте

    while True:
        user_choice = scoreboard.get_user_choice()
        computer_choice = scoreboard.get_computer_choice()
        print(f'user_choice = {user_choice}; computer_choice = {computer_choice}')
        result = scoreboard.determine_winner(user_choice, computer_choice)

        if result == "user":
            print("🏆 Вы победили в этом раунде!")
        elif result == "computer":
            print("😔 Компьютер победил в этом раунде.")
        elif result == "non wins":
            print("🤝 Ничья!")

        # Обновление счета
        scoreboard.update_score(result) 
        scoreboard.display_score() # Отображение обновленного счета


if __name__ == "__main__":
    main_game_loop()