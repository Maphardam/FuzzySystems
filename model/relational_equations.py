'''
Created on Dec 28, 2016

@author: tsabsch
'''

def goedel_implication(x, y):
    '''
    Goedel implication of two values x and y
    The Goedel implication is defined as 1, if x is smaller than y, and y 
    otherwise.
    ''' 
    if x <= y:
        return 1
    return y


def greatest_solution(X, Y, fuzzy_set_X, fuzzy_set_Y):
    '''
    X and Y are two finite crisp sets.
    fuzzy_set_X and fuzzy_set_Y are two fuzzy sets that are defined on X and Y 
    respectively.
    '''
    len_X = len(X)
    len_Y = len(Y)

    solution = [0] * len_X * len_Y
    for i in range(0,len_X):
        for j in range(0,len_Y):
            solution[i*len_Y + j] = goedel_implication(
                fuzzy_set_X.get_membership_value(X[i]), 
                fuzzy_set_Y.get_membership_value(Y[j]))

    return solution


def greatest_solution_for_all(X, Y, fuzzy_sets_X, fuzzy_sets_Y):
    '''
    X and Y are two finite crisp sets.
    fuzzy_sets_X and fuzzy_sets_Y are two lists of fuzzy sets that are defined 
    on X and Y respectively and have the same number of fuzzy sets (named r in 
    formulas).
    '''
    num_eq = len(fuzzy_sets_X)
    eq_solutions = [0]*num_eq

    # compute single goedel solutions
    for r in range(0, num_eq):
        eq_solutions[r] = greatest_solution(X, Y, fuzzy_sets_X[r], fuzzy_sets_Y[r])

    # compute global solution
    len_X = len(X)
    len_Y = len(Y)

    solution = [0] * len_X * len_Y
    for i in range(0,len_X):
        for j in range(0,len_Y):
            solution[i*len_Y + j] = min(
                [eq_solutions[r][i*len_Y + j] for r in range(0,num_eq)])

    return solution