import random

random_number = random.randint(1, 20)

user_number = int(
    input(
        "Я загадал число от 1 до 20. Введите число, чтобы попробовать угадать: (всего 5 попыток) "
    )
)

counter = 5  # Количество попыток

while user_number != random_number and counter > 1:
    counter -= 1
    if user_number < random_number:
        print(f"Загаданное число больше. Осталось попыток: {counter}")
    else:
        print(f"Загаданное число меньше. Осталось попыток: {counter}")
    user_number = int(input("Попробуйте еще раз: "))

if random_number == user_number:
    print(f"Поздравялем, вы угадали загаданное число: {random_number}")
else:
    print(f"К сожалению вы проиграли. Загаданное число было: {random_number}")
