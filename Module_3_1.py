# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).


# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info (string1):
    a = (len(string1), string1.upper(), string1.lower())
    print(string1)

    n = count_calls()
    return a

def is_contains (string, *list_to_search):
    global result_1
    list_1 = string.lower()
    list_6 = list_to_search[0]
    z = 0
    while z < len(list_6):
        list_6[z] = list_6[z].lower()
        list_joined = ''.join(list_6)
        index_2 = list_joined.find(list_1)
        if (index_2 < 0):
            result_1 = 'False'
        elif (index_2 > 0):
            result_1 = 'True'
            break
        z += 1
    count_calls()
    return result_1

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print (is_contains('boom',['baDaoom', 'BADAbadaOm','BadaBOOM']))
print (is_contains('bamm',['baDaoom', 'BADAbadaOm','BadaBOOM']))
print('calls: ',calls)