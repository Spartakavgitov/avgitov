# TODO Напишите функцию для поиска индекса товара
def find_needed_items(items_list, find_item):  # создаем функцию с уже имеющимися переменными
    if find_item in items_list:  # если во множестве найдется нужный товар выводим индекс, если нет то None
        return items_list.index(find_item)
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_needed_items(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
