# Определение максимально возможного дохода от вклада

# Процентные ставки банков
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Сумма вклада клиента
money = float(input("Введите сумму вклада: "))

# Накопленные средства за год по каждому банку в виде списка
deposit = [round(money*x/100.0, 2) for x in list(per_cent.values())]
#print(deposit)

print(f"Максимальная сумма, которую вы можете заработать — {max(deposit):.2f}")
