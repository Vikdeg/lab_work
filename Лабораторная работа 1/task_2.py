# TODO Найдите количество книг, которое можно разместить на дискете

change = 1024 # измерение разниц объема диска

inf_volume = 1.44 # объем дискеты в Мб
pages_1 = 100 # количество страниц в 1 книге
lines_page_1 = 50 # число строк на 1 странице
symbol_line = 25 # кол. символов в 1 строке
baggagge_symbol = 4 # объем для хранения 1 символа

book_1 = symbol_line * lines_page_1 * pages_1 # кол. символов в 1 книге
baggagge_book_1 = book_1 * baggagge_symbol # объем 1 книги в байтах

bag_book_1_mb = (baggagge_book_1 / change) / change # измерение в Мб 1 книги

books = inf_volume // bag_book_1_mb

print("Количество книг, помещающихся на дискету:", int(books))