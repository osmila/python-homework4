import generate_random_data


def find_sets_diff():
    set_A = generate_random_data.create_set(string_add=False)
    set_B = generate_random_data.create_set(string_add=False)
    print(f'Test sets are:\nA: {set_A}\nB: {set_B}')

    diff_set = set_A - set_B

    if len(diff_set) == 0:
        print('There are NO elements in set A that are not presented in set B')
    else:
        print(f'Difference between set A and set B: {diff_set}')


def delete_diff_set():
    set_A = generate_random_data.create_set(string_add=False)
    set_B = generate_random_data.create_set(string_add=False)
    print(f'Test sets are:\nA: {set_A}\nB: {set_B}')

    set_A = set_A - set_B

    if len(set_A) == 0:
        print('There are NO elements left in set A')
    else:
        print(f'Set A after deleting set B from it: {set_A}')


def custom_diff_list():
    list_A = generate_random_data.generate_list_random(list_max_length=5)
    list_B = generate_random_data.generate_list_random(list_max_length=5)
    print(f'Test lists are:\nA: {list_A}\nB: {list_B}')
    result_list_custom = list()
    result_set_diff = set(list_A) - set(list_B)

    for x in list_A:
        result_list_custom.append(x)

    for y in list_B:
        if y in result_list_custom:
            result_list_custom.remove(y)

    result_list_custom = list(set(result_list_custom))

    print('Custom diff:')
    if len(result_list_custom) == 0:
        print('There are NO elements in list A that are not presented in list B')
    else:
        print(f'Difference between list A and list B: {result_list_custom}')

    print('Built-in diff:')
    if len(result_set_diff) == 0:
        print('There are NO elements in set A that are not presented in set B')
    else:
        print(f'Difference between set A and set B: {result_set_diff}')