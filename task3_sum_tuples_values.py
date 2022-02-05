import generate_random_data
from itertools import zip_longest


def sum_tuples_elements():
    list_tuples = generate_random_data.create_list_of_tuples(tuples_max_count=4, string_add=False)

    print("Initial tuples:")
    for x in list_tuples:
        print(x)

    zipped_list = list(zip_longest(*list_tuples, fillvalue=0))

    sum_list = list()
    for x in zipped_list:
        sum = 0
        for i in range(len(x)):
            sum += x[i]
        sum_list.append(sum)
    result_tuple = tuple(sum_list)
    print(f'Resul tuple: {result_tuple}')


