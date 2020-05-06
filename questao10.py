def answer_anything(function):
    def searching_for_solution():
        func = function()
        sol = 'anything can answer '
        return sol + func
    return searching_for_solution

def anything(function):
    def the_right_anything():
        func = function()
        anyth = 'The right '
        return anyth + func
    return the_right_anything
    
@anything
@answer_anything
def a_difficult_quesiton():
    return 'the most difficult question'



print(a_difficult_quesiton())