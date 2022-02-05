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


def custom_diff_set():
    set_A = generate_random_data.create_set(string_add=False)
    set_B = generate_random_data.create_set(string_add=False)
    print(f'Test sets are:\nA: {set_A}\nB: {set_B}')
    result_set_custom = set()
    result_set_diff = set()
    result_set_diff = set_A - set_B

    for x in set_A:
        result_set_custom.add(x)

    for y in set_B:
        if y in result_set_custom:
            result_set_custom.remove(y)

    print('Custom diff:')
    if len(result_set_custom) == 0:
        print('There are NO elements in set A that are not presented in set B')
    else:
        print(f'Difference between set A and set B: {result_set_custom}')

    print('Built-in diff:')
    if len(result_set_custom) == 0:
        print('There are NO elements in set A that are not presented in set B')
    else:
        print(f'Difference between set A and set B: {result_set_diff}')