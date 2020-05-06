def sum_in_a_strange_way(list, dictionary):
    return list[0] + list[1] + dictionary["number1"] + dictionary["number2"]


l = [1 , 2]
d = {"number1": 1, "number2": 2}

print(sum_in_a_strange_way(l, d))