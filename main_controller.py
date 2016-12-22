'''
Created on Dec 22, 2016

@author: crekowski
'''
from model.fuzzy_set import FuzzySet
from interface import controller_dialog_manager as controller_dm
from interface import alphacut_dialog_manager as alphacut_dm
from model import relational_equations as req


def build_fuzzy_set():
    # Create fuzzy set
    fuzzy_set = FuzzySet()
    
    # Get list of degrees from user input
    degrees = alphacut_dm.get_degree_input()
    
    # Get the cuts for each degree from user input
    for degree in degrees:
        cuts = alphacut_dm.get_alpha_cut_input(degree)
        fuzzy_set.add_cuts_for_degree(degree, cuts)
    
    return fuzzy_set


def get_fuzzy_sets(keys):
    X = dict()
    
    for k in keys:
        print "Please provide a fuzzy set for {}.".format(k)
        X[k] = build_fuzzy_set()
    
    return X


if __name__ == '__main__':
    print "### Welcome to the Fuzzy Controller Master! ###"
    
    # Let the user enter finite crisp sets X and Y
    X_keys = controller_dm.get_finite_crisp_set()
    Y_keys = controller_dm.get_finite_crisp_set()
    
    # Let the user enter r fuzzy sets on X and Y
    X = get_fuzzy_sets(X_keys)
    Y = get_fuzzy_sets(Y_keys)

    print(X)
    print(Y)
    
    # Calculate the greatest solution for the relational equations given by the
    # fuzzy sets on X and Y
    solution = req.greatest_solution_for_all(X, Y)
    
    # TODO: Show the solution
    