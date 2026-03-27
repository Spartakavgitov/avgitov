salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
capital_needed = 0

for month in range(1, months + 1):
    current_spend = spend * (1 + increase) ** (month - 1)  # Используем month-1, так как в 1-м месяце increase^0 = 1
    deficit = max(0, current_spend - salary)  # Дефицит, который нужно покрыть из подушки

    capital_needed += deficit  # Добавляем к общей необходимой сумме
    round_capital = round(capital_needed)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round_capital)
