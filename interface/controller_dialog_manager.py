'''
Created on Dec 22, 2016

@author: crekowski
'''
import input_parser as ip


def get_finite_crisp_set():
    print "You can give arbitrary elements separated by ','."
    
    elements = None
    while elements is None:
        elements_string = raw_input(">>> ")
        
        # Read elements from the given input
        elements = ip.read_list(elements_string)
    
    return elements


def get_membership_value(x):
    membership_value = None
    while membership_value is None:
        mv_string = raw_input("{} >>> ".format(x)) 
        
        membership_value = ip.read_membership_value(mv_string)
        
        if membership_value is None:
            # Input could not be parsed, try again
            print "Please provide a value in the interval [0, 1]!"
    
    return membership_value


def add_sets():
    print "Do you want to add more fuzzy sets? (yes/no)"
    
    response = raw_input(">>> ")
    
    if response.lower().strip() == "yes":
        return True
    else:
        return False
