import random
import string


def generate_list_random(numbers_exist=True, string_exist=False, string_max_length=5):
    length = random.randrange(1, 20)
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


def convert_list_to_tuple():
    initial_list = generate_list_random(string_exist=True)
    result_tuple = tuple(initial_list)
    print(f'Initial list:\t{initial_list}')
    print(f'Result tuple:\t{result_tuple}')