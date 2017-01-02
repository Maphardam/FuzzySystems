"""
Created on Dec 22, 2016.

@author: crekowski
"""

import input_parser as ip


def get_degree_input():
    """Get degree from user.

    Returns:
        A list containing the degrees.
    """
    print "Please provide the list of relevant degrees of membership."
    print "You can give the values separated by ','."
    print "The degrees need to be between 0 and 1 (inclusive)."

    degrees = None
    while degrees is None:
        degree_string = raw_input(">>> ")

        # Read values from the given input
        degrees = ip.read_number_list(degree_string)

        if degrees is not None and \
           (any(d < 0 for d in degrees) or any(d > 1 for d in degrees)):
            # Invalid value for a degree
            degrees = None

        if degrees is None:
            # Input could not be parsed, try again
            print "You have used the wrong format! Please try again."

    # Sort list of degrees so that later on high degrees are processed first
    degrees.sort(reverse=True)

    return degrees


def get_alpha_cut_input(degree):
    """Get alpha cut from user.

    Args:
        degree: Degree value

    Returns:
        A list representing the value range having the requested degree.
    """
    print "Please provide alpha cuts for the following degree."
    print "Your input should have the format: a1 b1,a2 b2, ..."
    print "Single values are also allowed."

    degree_cuts = None
    while degree_cuts is None:
        cut_string = raw_input("{} >>> ".format(degree))

        # Read cuts form the given input
        degree_cuts = ip.read_cut_values(cut_string)

        if degree_cuts is None:
            print "You have used the wrong format! Please try again."

    # Save cutes in data structure
    return degree_cuts


def get_request():
    """Get a request.

    Returns:
        A boolean representing whether a request was made. If yes, the request
        itself is returned as the second value.
    """
    print "Which membership degree do you want to know?"
    print "You can simply enter the point of interest or type 'end' to finish."

    inp = raw_input(">>> ")

    if inp.lower().strip() == 'end':
        # End loop
        return False, None
    else:
        # Parse input and calculate membership value
        x = ip.read_x_value(inp)

        if x is None:
            print "You have used the wrong format! Please try again."
            return True, None
        else:
            return True, x
