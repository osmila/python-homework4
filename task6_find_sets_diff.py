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