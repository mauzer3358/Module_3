data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


List_numbers = []
result = 0

def List_int (list):
    num_int_list = []
    for j in list:
        if type(j) == int:
            num_int_list.append(j)
    return num_int_list

def List_dict (dict):
    cort_keys = dict.keys()
    cort_values = dict.values()
    num_dict_list = []
    for j in cort_keys:
        num_dict_list.append(len(j))
    for k in cort_values:
        num_dict_list.append(k)
    return num_dict_list


def List_str (string):
    a = len(string)
    num_str_list = []
    num_str_list.append(a)
    return num_str_list

def List_tuple (tuple):
    tuple_list = []
    for i in tuple:
        tuple_list.append(i)
    return tuple_list

def Lis_set (set):
    set_list = []
    for i in set:
        set_list.append(i)
    return set_list

def calculate_structure_sum (data_structure):
    List = SEARCH(data_structure)
    summa = 0
    for i in List:
        for j in i:
            summa = summa + j
    print(summa)
    return summa


def SEARCH (data_structure):
    global List_numbers
    for i in data_structure:
        if type(i) == int:
            List_numbers.append([i])
        elif type(i) == list:
            for j in i:
                if type(j) == int:
                    num = List_int([j])
                    List_numbers.append(num)
                else:
                    List_set = []
                    for k in j:
                        for l in k:
                            if type(l) == int:
                                List_numbers.append([l])
                            elif type(l) == str:
                                num = List_str(l)
                                List_numbers.append(num)
                            elif type(l) == tuple:
                                aaa = List_tuple(l)
                                bbb = SEARCH(aaa)
        elif type(i) == dict:
            num = List_dict(i)
            for z in num:
                List_numbers.append([z])
        elif type(i) == str:
            num = List_str(i)
            List_numbers.append(num)
        elif type(i) == tuple:
            num = list(List_tuple(i))
            num1 = SEARCH(num)
    return List_numbers


result = calculate_structure_sum(data_structure)