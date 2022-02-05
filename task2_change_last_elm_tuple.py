import generate_random_data


def change_last_tuple_element_in_list(changed_value):
    list_to_update = generate_random_data.create_list_of_tuples()
    result_list = list()
    print(f'Initial list:\t{list_to_update}')
    for i in range(len(list_to_update)):
        list_temp = list(list_to_update[i])
        list_temp[len(list_temp)-1] = changed_value
        result_list.append(tuple(list_temp))
    print(f'Result list:\t{result_list}')
