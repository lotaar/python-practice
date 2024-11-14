total_seconds = int(input("Введите количество секунд: "))


hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, minutes, seconds, sep=":")  # Выводим результат в формате Ч:М:С
