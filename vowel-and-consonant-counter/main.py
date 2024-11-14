string = input("Введите строку: ")

# Гласные буквы
vowels_split = ["А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]

# Согласные буквы
consonants_split = [
    "Б",
    "В",
    "Г",
    "Д",
    "Ж",
    "З",
    "Й",
    "К",
    "Л",
    "М",
    "Н",
    "П",
    "Р",
    "С",
    "Т",
    "Ф",
    "Х",
    "Ц",
    "Ч",
    "Ш",
    "Щ",
]

vowels = 0
consonants = 0
# Приводим строку к верхнему регистру для корректного сравнения
string = string.upper()
# Перебираем каждый символ в строке
for char in string:
    if char in vowels_split:  # Проверка, является ли символ гласной
        vowels += 1
    elif char in consonants_split:  # Проверка, является ли символ согласной
        consonants += 1
print("Гласных: ", vowels, "Согласных: ", consonants)
