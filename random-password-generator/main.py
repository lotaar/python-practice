import string
import random

password_length = int(
    input("Введите желаемое количество символов в пароле (не меньше 6): ")
)
use_special_characters = input("Использовать спецсимволы в пароле? (да/нет): ").lower()
if use_special_characters == "да":
    use_special_characters = True
else:
    use_special_characters = False
characters = string.ascii_letters + string.digits

if use_special_characters:
    characters += string.punctuation

if password_length < 6:
    print(
        "Длина пароля не может быть меньше 6 симоволов, устанавливаем значение по умлочанию (6)"
    )
    password_length = 6

password = "".join(random.choice(characters) for i in range(password_length))

print(password)
