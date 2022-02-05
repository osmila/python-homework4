import random
import string


def generate_list_random(numbers_exist=True, string_exist=False,
                         string_max_length=5, list_min_length=1, list_max_length=20):
    length = random.randrange(list_min_length, list_max_length)
    my_list = list()
    if numbers_exist == True and string_exist == False:
        for _ in range(length):
            my_list.append(random.randrange(1, 10))
    elif numbers_exist == False and string_exist == True:
        for _ in range(length):
            word_length = random.randrange(1, string_max_length)
            new_word = ''.join(random.choice(string.ascii_letters) for i in range(word_length))
            my_list.append(new_word)
    elif numbers_exist == True and string_exist == True:
        for _ in range(length):
            is_number = random.choice([True, False])
            if is_number:
                my_list.append(random.randrange(1, 10))
            else:
                word_length = random.randrange(1, string_max_length)
                new_word = ''.join(random.choice(string.ascii_letters) for i in range(word_length))
                my_list.append(new_word)
    else:
        my_list = list()
    return my_list


def create_list_of_tuples(tuples_max_count=5, string_add=True):
    tuples_count = random.randrange(1, tuples_max_count)
    list_tuples = list()
    for i in range(tuples_count):
        temp_list = generate_list_random(string_exist=string_add, list_min_length=2, list_max_length=6)
        list_tuples.append(tuple(temp_list))
    return list_tuples
