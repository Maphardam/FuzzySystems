'''
Created on Dec 22, 2016

@author: crekowski
'''
import input_parser as ip


def get_finite_crisp_set():
    print "Please provide a finite crisp set (only numbers allowed)."
    print "You can give the values separated by ','."
    
    elements = None
    while elements is None:
        elements_string = raw_input(">>> ")
        
        # Read values from the given input
        elements = ip.read_number_list(elements_string)
        
        if elements is None:
            # Input could not be parsed, try again
            print "You have used the wrong format! Please try again."
    
    return elements