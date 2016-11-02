'''
Created on Oct 28, 2016

@author: cornelius
'''
import visualize
from collections import OrderedDict

def read_degree_values(degree_string):
    try:
        # split list by ','
        return [float(s.strip()) for s in degree_string.split(',')]
    except ValueError:
        # something was not a float in there
        return None

def read_cut_values(cut_string):
    try:
        # split given string into list of separate cuts
        cut_list = [cut.split() for cut in cut_string.split(',')]
        
        # read lower and upper boundary from each cut
        cut_tuples = []
        for bounds in cut_list:
            if len(bounds) == 2:
                a = bounds[0]
                b = bounds[1]
            elif len(bounds) == 1:
                # exactly one value defined -> use as upper and lower boundary
                a = bounds[0]
                b = a
            else:
                # too many or no values defined
                return None
            
            cut_tuples.append((float(a.strip()), float(b.strip())))
        
        return cut_tuples
    
    except ValueError:
        # something was not a float in there
        return None

def read_x_value(x_string):
    try:
        return float(x_string.strip())
    except ValueError:
        return None

def get_degree_input():
    print "Please provide the list of relevant degrees of membership."
    print "You can give the values separated by ','."
    print "The degrees need to be between 0 and 1 (inclusive)."
    
    degrees = None
    while degrees is None:
        degree_string = raw_input(">>> ")
        
        # read values from the given input
        degrees = read_degree_values(degree_string)
        
        if not degrees is None and \
           (any(d < 0 for d in degrees) or any(d > 1 for d in degrees)):
            # invalid value for a degree
            degrees = None
        
        if degrees is None:
            # input could not be parsed, try again
            print "You have used the wrong format! Please try again."
    
    # sort list of degrees so that later on high degrees are processed first
    degrees.sort(reverse=True)
    
    return degrees

def get_alpha_cut_input(degrees):
    print "Please provide alpha cuts for the following degrees."
    print "Your input should have the format: a1 b1,a2 b2, ..."
    print "Single values are also allowed."
    
    alpha_cuts = OrderedDict()
    for degree in degrees:
        degree_cuts = None
        while degree_cuts is None:
            cut_string = raw_input("{} >>> ".format(degree))
            
            # read cuts form the given input
            degree_cuts = read_cut_values(cut_string)
            
            if degree_cuts is None:
                print "You have used the wrong format! Please try again."
        
        # save cutes in data structure
        alpha_cuts[degree] = degree_cuts
    
    return alpha_cuts

def get_membership_value(alpha_cuts, x):
    # traverse alpha-cuts from high to low degrees of membership
    for degree, cuts in alpha_cuts.items():
        # traverse all ranges for this degree
        for a, b in cuts:
            if a <= x and x <= b:
                # x is located in this cut -> highest matching degree
                return degree
    
    # no matching degree -> support is 0
    return 0.0


def handle_requests(alpha_cuts):
    print "Which membership degree do you want to know?"
    print "You can simply enter the point of interest or type 'end' to finish."
    
    run = True
    while run:
        inp = raw_input(">>> ")
        
        if inp.lower().strip() == 'end':
            # end loop
            run = False
        else:
            # parse input and calculate membership value
            x = read_x_value(inp)
            
            if x is None:
                print "You have used the wrong format! Please try again."
            else:
                mem = get_membership_value(alpha_cuts, x)
                print "Membership value: {}".format(mem)
                visualize.visualize_x(alpha_cuts, x)


if __name__ == '__main__':
    print "### Welcome to the Alpha-Cut Master! ###"
    
    # build data structure from user input
    degrees = get_degree_input()
    alpha_cuts = get_alpha_cut_input(degrees)

    # show alpha cuts
    visualize.visualize(alpha_cuts, kind='upper_envelope')
    
    # allow requests
    handle_requests(alpha_cuts)
    
    print "We hope you enjoyed using the Alpha-Cut Master!"
