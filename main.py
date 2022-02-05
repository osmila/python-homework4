import generate_random_data
import task1_convert_list_to_tuple
import task2_change_last_elm_tuple
import task3_sum_tuples_values
import task4_value_in_set_exists
import task5_sets_have_common_values
import task6_find_sets_diff
import task8_custom_union

# Task 1:
# Напишите программу для преобразования списка в кортеж
print('Task 1: Convert list to tuple:')
task1_convert_list_to_tuple.convert_list_to_tuple()

# Task 2:
# Напишите программу для замены последнего значения кортежей в списке
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
print('\nTask 2: Change last tuple value in the list:')
task2_change_last_elm_tuple.change_last_tuple_element_in_list(100)

# Task 3:
# Напишите программу для поэлементного вычисления суммы
# заданных кортежей. Результатом должен быть кортеж.
print('\nTask 3: Calculate sum of tuples values:')
task3_sum_tuples_values.sum_tuples_elements()

# Task 4:
# Напишите программу, которая проверяет, присутствует ли А в
# наборе или нет. А вводится с клавиатуры
print('\nTask 4: Check if entered value exists in the set:')
task4_value_in_set_exists.check_value_in_set_exists()

# Task 5:
# Напишите программу, чтобы проверить, не имеют ли два
# заданных набора (set) общих элементов.
print('\nTask 5: Check if 2 sets have common values:')
task5_sets_have_common_values.check_2_sets_contain_common_values()

# Task 6:
# Напишите программу для поиска элементов в данном наборе A
# (set), которых нет в другом наборе B.
print('\nTask 6: Find the difference between 2 sets:')
task6_find_sets_diff.find_sets_diff()

# Task 7:
# Напишите программу, которая удаляет пересечение 2-го набора
# из 1-го набора.
print('\nTask 7: Delete the difference between 2 sets from 1st one:')
task6_find_sets_diff.delete_diff_set()


# Task 8:
# Реализовать логику Union для двух списков (list), проверить работу
# алгоритма на set.union
print('\nTask 8: Custom union function:')
test_sets_list = generate_random_data.create_list_of_sets(string_add=False)
task8_custom_union.custom_union(test_sets_list)

# Task 9:
# Реализовать логику Difference для двух списков (list), проверить работу
# алгоритма на set.difference
print('\nTask 9: Custom difference function:')
task6_find_sets_diff.custom_diff_set()