def conv_to_dict(coord_list):
    my_list = coord_list
    my_dict = {}

    for index, element in enumerate(my_list):
        my_dict[index+1] = element

    return my_dict
