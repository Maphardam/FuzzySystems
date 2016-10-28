'''
Created on Oct 28, 2016

@author: cornelius
'''

def read_degree_values(degree_string):
    # TODO: handle bad input
    return [float(s.strip()) for s in degree_string.split(',')]

def read_cut_values(cuts_string):
    # TODO: support single values as both lower and upper boundary
    # TODO: handle bad input
    cuts_list = [cut.split() for cut in cuts_string.split(',')]
    return [(float(a.strip()), float(b.strip())) for a, b in cuts_list]


if __name__ == '__main__':
    # get user input for the list of relevant degrees
    print "Welcome to the Alpha-Cut master!"
    print "Please provide the list of relevant degrees of membership for " + \
          "your data structure. You can give the values separated by ','."
    degree_string = raw_input(">>> ")
    
    # read values from the given input
    degrees = read_degree_values(degree_string)
    
    # create empty data structure
    alpha_cuts = {}
    
    # get user input for the actual alpha cuts
    print "Please provide alpha cuts for the following degrees. Your input " + \
          "should have the format: a1 b1,a2 b2, ..."
    for degree in degrees:
        cuts_string = raw_input("{} >>> ".format(degree))
        
        # read cuts form the given input
        degree_cuts = read_cut_values(cuts_string)
        
        # save cutes in data structure
        alpha_cuts[degree] = degree_cuts
    
    print "Done!"
