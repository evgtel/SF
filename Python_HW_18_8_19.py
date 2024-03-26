# Подсчет стоимости билетов на онлайн-конференцию

# Регистрация:
member_count = int(input("Введите количество участников: "))

# Запрос возраста участников
members = [int(input(f"Возраст участника {i}: ")) for i in range(1, member_count+1)]

# Подсчет стоимости билетов:
sum = 0
for age in members:
    if age >=18 and age <25:
        sum += 990
    elif age >=25:
        sum += 1390
if len(members) >3: # Если участников > 3 скидка 10%
    sum *= 0.9
print(f"Стоимость билетов: {sum}")
