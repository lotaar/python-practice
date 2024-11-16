dog_years = int(input("Введите возраст собаки: "))
FIRST_TWO_YEARS_RATE = 10.5
OTHER_YEARS_RATE = 4

if dog_years <= 2:
    human_age = dog_years * FIRST_TWO_YEARS_RATE
else:
    human_age = (2 * FIRST_TWO_YEARS_RATE) + ((dog_years - 2) * OTHER_YEARS_RATE)
print(f"Возраст собаки в человеческих годах: {human_age}")
