import generate_random_data


def custom_union_sets(test_sets):
    result_set_custom = set()
    result_set_union = set()
    print(f'Initial test sets:')
    for test_set in test_sets:
        print(test_set)
        result_set_union = result_set_union.union(test_set)
        for x in test_set:
            result_set_custom.add(x)
    print(f'Custom union:\t{result_set_custom}')
    print(f'Built-in union:\t{result_set_union}')


def custom_union_lists():
    list_A = generate_random_data.generate_list_random(list_max_length=5)
    list_B = generate_random_data.generate_list_random(list_max_length=5)
    print(f'Test lists are:\nA: {list_A}\nB: {list_B}')
    result_list_custom = list()
    result_set_union = set(list_A).union(set(list_B))

    for x in list_A:
        result_list_custom.append(x)
    for y in list_B:
        result_list_custom.append(y)

    result_list_custom = list(set(result_list_custom))

    print(f'Custom union:\t{result_list_custom}')
    print(f'Built-in union:\t{result_set_union}')