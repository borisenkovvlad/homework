int_list = [1.1, 78, 4.5, 10, -100]


def apply_all_func(int_list, *functions):
    reuslts = {}
    for function in functions:
        reuslts.update({function.__name__: function(int_list)})
    return reuslts


def min(list_):
    min_number = 10 ** 100
    for i in list_:
        if i < min_number:
            min_number = i
    return min_number


def max(list_):
    max_number = -1 * 10 ** 100
    for i in list_:
        if i > max_number:
            max_number = i
    return max_number


def len_(list_):
    return len(list_)


def sum_(list_):
    return sum(list_)


def sorted_(list_):
    return sorted(list_)


def only_float(list_):
    float_lst = []
    for i in list_:
        if isinstance(i, float):
            float_lst.append(i)
    return float_lst


def only_int(list_):
    int_lst = []
    for i in list_:
        if isinstance(i, int):
            int_lst.append(i)
    return int_lst


print(apply_all_func(int_list, only_float, only_int, sorted_))
