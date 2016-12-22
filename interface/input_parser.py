'''
Created on Dec 22, 2016

@author: crekowski
'''

def read_degree_values(degree_string):
    try:
        # Split list by ','
        return [float(s.strip()) for s in degree_string.split(',')]
    except ValueError:
        # Something was not a float in there
        return None


def read_cut_values(cut_string):
    try:
        # Split given string into list of separate cuts
        cut_list = [cut.split() for cut in cut_string.split(',')]
        
        # Read lower and upper boundary from each cut
        cut_tuples = []
        for bounds in cut_list:
            if len(bounds) == 2:
                a = bounds[0]
                b = bounds[1]
            elif len(bounds) == 1:
                # Exactly one value defined -> use as upper and lower boundary
                a = bounds[0]
                b = a
            else:
                # Too many or no values defined
                return None
            
            cut_tuples.append((float(a.strip()), float(b.strip())))
        
        return cut_tuples
    
    except ValueError:
        # Something was not a float in there
        return None


def read_x_value(x_string):
    try:
        return float(x_string.strip())
    except ValueError:
        return None
