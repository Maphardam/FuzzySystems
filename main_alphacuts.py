'''
Created on Oct 28, 2016

@author: crekowski
'''
from model.fuzzy_set import FuzzySet
from interface import alphacut_dialog_manager as dm
from visualization import visualize_fuzzy_set as vis


def build_fuzzy_set():
    # Create fuzzy set
    fuzzy_set = FuzzySet()
    
    # Get list of degrees from user input
    degrees = dm.get_degree_input()
    
    # Get the cuts for each degree from user input
    for degree in degrees:
        cuts = dm.get_alpha_cut_input(degree)
        fuzzy_set.add_cuts_for_degree(degree, cuts)
    
    return fuzzy_set


def handle_requests(fuzzy_set, fig):
    line, default_xticks = vis.init_handler(fig)
    
    run = True
    while run:
        run, x = dm.get_request()
        
        if not x is None:
            mem = fuzzy_set.get_membership_value(x)
            print "Membership value: {}".format(mem)
            line = vis.visualize_x(fig, line, default_xticks, x, mem)


if __name__ == '__main__':
    print "### Welcome to the Alpha-Cut Master! ###"
    
    # Build fuzzy set from user input
    fuzzy_set = build_fuzzy_set()
    
    # Show fuzzy set
    fig = vis.visualize(fuzzy_set)
    
    # Handle requests
    handle_requests(fuzzy_set, fig)
    
    print "We hope you enjoyed using the Alpha-Cut Master!"
