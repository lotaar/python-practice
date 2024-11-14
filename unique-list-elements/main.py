list_items = input("Введите числа через пробел: ")
numbers_list = [int(num) for num in list_items.split()]
unique_numbers = []
# Проходим по всем числам в numbers_list
for num in numbers_list:
    if num not in unique_numbers:  # Если числа нет в unique_numbers, добавляем его
        unique_numbers.append(num)


print(unique_numbers)
