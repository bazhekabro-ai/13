import random
import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_choice():
    while True:
        user_input = input("Введите свой выбор (камень, ножницы, бумага): ").strip().lower()
        if user_input in ['камень', 'ножницы', 'бумага']:
            return user_input
        else:
            print("Некорректный ввод. Попробуйте снова.")

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы победили"
    else:
        return "Вы проиграли"

def play_game():
    # Запрашиваем у пользователя количество побед для завершения игры
    while True:
        try:
            target_score = int(input("Введите количество побед для завершения игры: "))
            if target_score > 0:
                break
            else:
                print("Количество побед должно быть больше 0. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    user_score = 0
    computer_score = 0

    while user_score < target_score and computer_score < target_score:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        # Логирование
        logging.info(f"Игрок: {user_choice}, Компьютер: {computer_choice}, Результат: {result}")

        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        print(result)

        if result == "Вы победили":
            user_score += 1
        elif result == "Вы проиграли":
            computer_score += 1

        print(f"Текущий счет: Игрок - {user_score}, Компьютер - {computer_score}")

    if user_score == target_score:
        print("Вы выиграли игру!")
    else:
        print("Вы проиграли игру.")

if __name__ == "__main__":
    play_game()