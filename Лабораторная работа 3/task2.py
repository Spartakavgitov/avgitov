# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, delimiter=','):  # фуекция принимающая нужные переменные
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)
    common = list(set([p for p in participants1 if p in participants2]))  # ищем совпадения в списках
    return sorted(common)  # преобразовав список во множество и обратно в список, сортируем его
# TODO Провеьте работу функции с разделителем отличным от запятой


result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)  # ['Петров', 'Сидоров']

group1_default = "Иванов,Петров,Сидоров"
group2_default = "Петров,Сидоров,Смирнов"
result_default = find_common_participants(group1_default, group2_default)
print(result_default)