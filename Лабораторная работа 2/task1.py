money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
capital = money_capital
months = 0
current_spend = spend

while True:
    budget = salary + capital
    if current_spend > budget:  # пока траты не будут превышать бюджет цикл будет продолжаться
        break
    capital = budget - current_spend  # после траты salary, остаток current_spend будет вычетаться из подушки
    current_spend *= (1 + increase)  # изменение трат со временем
    months += 1 # счет месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months )
