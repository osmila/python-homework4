import generate_random_data


def check_value_in_set_exists():
    test_set = generate_random_data.create_set()
    print(f'Test set is: {test_set}')
    test_value = input('Enter value to check if set contains it: ')
    if test_value.isdigit():
        test_value = int(test_value)
    value_in_set_exists = test_value in test_set
    print(value_in_set_exists)
    if value_in_set_exists:
        print('Test set contains the entered value')
    else:
        print('Test set does NOT contain the entered value')