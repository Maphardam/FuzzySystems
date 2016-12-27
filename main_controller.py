'''
Created on Dec 22, 2016

@author: crekowski
'''
from model.fuzzy_set import FuzzySet
from interface import controller_dialog_manager as controller_dm
from interface import alphacut_dialog_manager as alphacut_dm
from model import relational_equations as req


def build_fuzzy_set(crisp_set):
    # TODO: Is the underlying crisp set even needed for fuzzy set definition?
    
    # Create fuzzy set
    fuzzy_set = FuzzySet()
    
    # Get list of degrees from user input
    degrees = alphacut_dm.get_degree_input()
    
    # Get the cuts for each degree from user input
    for degree in degrees:
        cuts = alphacut_dm.get_alpha_cut_input(degree)
        fuzzy_set.add_cuts_for_degree(degree, cuts)
    
    return fuzzy_set


def get_fuzzy_sets(X, Y):
    fuzzy_sets_X = []
    fuzzy_sets_Y = []
    
    add_sets = True
    while add_sets:
        print "Please provide a fuzzy set on X ({}).".format(X)
        fsX = build_fuzzy_set(X)
        
        print "Please provide a fuzzy set on Y ({}).".format(Y)
        fsY = build_fuzzy_set(Y)
        
        fuzzy_sets_X.append(fsX)
        fuzzy_sets_Y.append(fsY)
        
        add_sets = controller_dm.add_sets()
    
    return fuzzy_sets_X, fuzzy_sets_Y


if __name__ == '__main__':
    print "### Welcome to the Fuzzy Controller Master! ###"
    
    # Let the user enter finite crisp sets X and Y
    X = controller_dm.get_finite_crisp_set()
    Y = controller_dm.get_finite_crisp_set()
    
    # Let the user enter r fuzzy sets on X and Y
    fuzzy_sets_X, fuzzy_sets_Y = get_fuzzy_sets(X, Y)
    
    # Calculate the greatest solution for the relational equations given by the
    # fuzzy sets on X and Y
    solution = req.greatest_solution_for_all(X, Y, fuzzy_sets_X, fuzzy_sets_Y)
    
    # TODO: Show the solution
    