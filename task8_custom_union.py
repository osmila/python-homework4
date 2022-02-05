def custom_union(test_sets):
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