# Домашка 10. Задача 1. Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и
#     среднее арифметическое последовательности целых чисел.
#     Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число, которое
#     будет учтено при вычислении финального результата методом result. Для экземпляров MinStat и MaxStat result должен
#     возвращать целое число, для AverageStat — число типа float (это число будет сравниваться с правильным ответом до
#     седьмой значащей цифры).
#     Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен
#     возвращать None.
#         Пример 1.
#             values = [1, 2, 4, 5]
#             mins = MinStat()
#             maxs = MaxStat()
#             average = AverageStat()
#             for v in values:
#                 mins.add_number(v)
#                 maxs.add_number(v)
#                 average.add_number(v)
#             print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
#         Пример 2.
#             mins = MinStat()
#             maxs = MaxStat()
#             average = AverageStat()
#             print(mins.result(), maxs.result(), average.result())
#         Пример 3.
#             values = [1, 0, 0]
#             mins = MinStat()
#             maxs = MaxStat()
#             average = AverageStat()
#             for v in values:
#                 mins.add_number(v)
#                 maxs.add_number(v)
#                 average.add_number(v)
#             print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


import func_stat

# Примеры из задания
print("Пример 1:")
values = [1, 2, 4, 5]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

print("Пример 2:")
values = [1, 2, 4, 5]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
print(mins.result(), maxs.result(), average.result())

print("Пример 3:")
values = [1, 0, 0]
mins = func_stat.MinStat()
maxs = func_stat.MaxStat()
average = func_stat.AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))






# # Домашка 10. Задача 2. Реализуйте класс Table, который хранит целые числа в двумерной таблице.
# #     При инициализации Table (rows, cols) экземпляру передаются число строк и столбцов в таблице.
# #     Строки и столбцы нумеруются с нуля.
# #         table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col.
# #                                     Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# #         table.set_value(row, col, value) — записать число в ячейку строки row, столбца col.
# #                                            Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# #         table.n_rows() — вернуть число строк в таблице
# #         table.n_cols() — вернуть число столбцов в таблице
# #         table.delete_row(row) — удалить строку с номером row
# #         table.delete_col(col) — удалить колонку с номером col
# #         table.add_row(row) — добавить в таблицу новую строку с индексом row.
# #                              Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.
# #         table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# #                              Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.
#
# import table as t
#
# print("Пример 1:")
# tab = t.Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(1)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# print("Пример 2:")
# tab = t.Table(2, 2)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(0)
# tab.add_col(1)
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# print("Пример 3:")
# tab = t.Table(1, 1)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.set_value(0, 0, 1000)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)
#
# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
