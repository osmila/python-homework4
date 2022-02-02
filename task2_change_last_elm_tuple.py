import task1_convert_list_to_tuple
import random


def create_list_of_tuples(tuples_max_count=5):
    tuples_count = random.randrange(1, tuples_max_count)
    list_tuples = list()
    for i in range(tuples_count):
        temp_list = task1_convert_list_to_tuple.generate_list_random(string_exist=True,
                                                                     list_min_length=2, list_max_length=6)
        list_tuples.append(tuple(temp_list))
    return list_tuples


def change_last_tuple_element_in_list():
    list_to_update = create_list_of_tuples()
    result_list = list()
    print(f'Initial list:\t{list_to_update}')
    for i in range(len(list_to_update)):
        list_temp = list(list_to_update[i])
        list_temp[len(list_temp)-1] = 100
        result_list.append(tuple(list_temp))
    print(f'Result list:\t{result_list}')