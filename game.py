import random
import sys
import os


class ScoreBoard:
    """Класс для управления счетом и сохранения результатов."""

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
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("🏆 Вы победили в этом раунде!")
        elif result == "computer":
            print("😔 Компьютер победил в этом раунде.")
        else:
            print("🤝 Ничья!")

        # Обновление счета
        scoreboard.update_score(result) 
        scoreboard.display_score() # Отображение обновленного счета


if __name__ == "__main__":
    main_game_loop()
