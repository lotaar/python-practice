string = input("Введите строку чтобы узнать является ли она палиндромом: ")

if string == string[::-1]:
    print("Является")
else:
    print("Не является")
