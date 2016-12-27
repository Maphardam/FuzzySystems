'''
Created on Dec 22, 2016

@author: crekowski
'''
from model.fuzzy_set import FuzzySetOnCrisp
from interface import controller_dialog_manager as controller_dm
from model import relational_equations as req


def build_fuzzy_set(crisp_set):
    # Create fuzzy set defined on the given crisp set
    fuzzy_set = FuzzySetOnCrisp(crisp_set)
    
    # Get the membership value for each element of the crisp set
    for x in crisp_set:
        membership_value = controller_dm.get_membership_value(x)
        fuzzy_set.add_value_for_x(x, membership_value)
    
    return fuzzy_set


def get_fuzzy_sets(X, Y):
    fuzzy_sets_X = []
    fuzzy_sets_Y = []
    
    print "Creating fuzzy implication rules on X and Y."
    
    add_sets = True
    while add_sets:
        print "Please provide membership values for the elements of X."
        fsX = build_fuzzy_set(X)
        
        print "Please provide membership values for the elements of Y."
        fsY = build_fuzzy_set(Y)
        
        fuzzy_sets_X.append(fsX)
        fuzzy_sets_Y.append(fsY)
        
        add_sets = controller_dm.add_sets()
    
    return fuzzy_sets_X, fuzzy_sets_Y


if __name__ == '__main__':
    print "### Welcome to the Fuzzy Controller Master! ###"
    
    # Let the user enter finite crisp sets X and Y
    print "Please provide the finite crisp set X."
    X = controller_dm.get_finite_crisp_set()
    print "Please provide the finite crisp set Y."
    Y = controller_dm.get_finite_crisp_set()
    
    # Let the user enter r fuzzy sets on X and Y
    fuzzy_sets_X, fuzzy_sets_Y = get_fuzzy_sets(X, Y)
    
    # Calculate the greatest solution for the relational equations given by the
    # fuzzy sets on X and Y
    solution = req.greatest_solution_for_all(X, Y, fuzzy_sets_X, fuzzy_sets_Y)
    
    print("Solution:")
    print(solution)
