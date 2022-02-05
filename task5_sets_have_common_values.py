import generate_random_data


def check_2_sets_contain_common_values():
    test_set_1 = generate_random_data.create_set(string_add=False)
    test_set_2 = generate_random_data.create_set(string_add=False)
    print(f'Test sets are:\n{test_set_1}\n{test_set_2}')

    intersection_set = test_set_1 & test_set_2

    if len(intersection_set) == 0:
        print('There are NO common values in test sets')
    else:
        print(f'There are {len(intersection_set)} common values in test sets: {intersection_set}')