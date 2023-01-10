def count(string):
    my_counter = {}
    for i in string:
        my_counter[i] = my_counter.get(i,0) + 1
    return my_counter

