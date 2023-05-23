# MARCOS FAJOLI DE ALMEIDA

# 01
def mult_list(list):
    result = 1 
    for x in list:
        result *= x
    
    return result

print(mult_list([5, 3, 2]))

# 02
def max_num(list):
    list.sort()
    return list[-1]

print(max_num([5, 7, 1, 2, 10, 5]))

# 03
def min_num(list):
    list.sort()
    return list[0]

print(min_num([5, 7, 1, 2, 10, 5]))

# 04
def del_duplicate(list):
    list0 = []
    for x in list:
        if x not in list0:
            list0.append(x)
    return list0

print(del_duplicate(['cabecao', 'gabriel', 'gabriel', 'reginaldo', 'douglas', 'cabecao']))

# 05
def is_empty(list):
    is_empty = True
    if len(list) > 0:
        is_empty = False
    
    return is_empty

print(is_empty([1]))

# 06
def clone_list(list):
    return list[:]

print(clone_list([1, 2, '20']))

# 07

def count_str(list):
    c = 0
    for x in list:
        if len(x) > 2 and x[0] == x[-1]:
            c += 1
    return c

print(count_str(['abc', 'xyz', 'aba', '1221', '11', '3555843']))
