# TODO Найдите количество книг, которое можно разместить на дискете
disket = 1.44
pages = 100
raws = 50
symbols = 25
one_symb = 4
symb_in_the_book = pages * raws * symbols * one_symb # найдем сколько весит одна книга в байтах
megabite = disket * 1024 * 1024 # кол-во бит в 1.44 мегабайтах
result = megabite / symb_in_the_book
 # получилось 3 с хвостом, дабы это убрать надо воспользоватся округлением в f-строках

print(f"Количество книг, помещающихся на дискету: {result:.0f}")
