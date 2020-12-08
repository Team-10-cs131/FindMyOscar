def tuple_to_dict(tuple, key_fields):
    dictionary = {}
    i = 0
    for key_field in key_fields:
        dictionary[key_field] = tuple[i]
        i += 1
    return dictionary


if __name__ == '__main__':
    test_tuple = (1, 2, 3)
    field_tuple = ('1', '2', '3')

    test_dict = tuple_to_dict(test_tuple, field_tuple)

    print(test_dict)