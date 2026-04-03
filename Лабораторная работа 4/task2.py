# TODO решите задачу
import json


def task() -> float:  # Определяем функцию task которая возвращает число с плавающей запятой (float)
    with open('data.json', 'r', encoding='utf-8') as file:  # Открываем файл 'data.json' в р.ч. ('r') с код. UTF-8
        data = json.load(file)

    total = sum(item['score'] * item['weight'] for item in data)  # суммa произведений для каждого словаря в списке
    return round(total, 3)


print(task())
