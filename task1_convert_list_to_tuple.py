import generate_random_data


def convert_list_to_tuple():
    initial_list = generate_random_data.generate_list_random(string_exist=True)
    result_tuple = tuple(initial_list)
    print(f'Initial list:\t{initial_list}')
    print(f'Result tuple:\t{result_tuple}')