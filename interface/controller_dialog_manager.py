"""
Created on Dec 22, 2016.

@author: crekowski
"""
import input_parser as ip


def get_finite_crisp_set():
    """Get crisp sets.

    The user is requested to enter the elements of a crisp set.

    Returns:
        The crisp set, stored as a list.
    """
    print "You can give arbitrary elements separated by ','."

    elements = None
    while elements is None:
        elements_string = raw_input(">>> ")

        # Read elements from the given input
        elements = ip.read_list(elements_string)

    return elements


def get_membership_value(x):
    """Get membership value for an element.

    Args:
        x: Value

    Returns:
        Membership value within [0,1] for x
    """
    membership_value = None
    while membership_value is None:
        mv_string = raw_input("{} >>> ".format(x))

        membership_value = ip.read_membership_value(mv_string)

        if membership_value is None:
            # Input could not be parsed, try again
            print "Please provide a value in the interval [0, 1]!"

    return membership_value


def add_sets():
    """Determine if another couple of fuzzy sets should be entered.

    Returns:
        Enter another couple of fuzzy sets (boolean)
    """
    print "Do you want to add more fuzzy sets? (yes/no)"

    response = raw_input(">>> ")

    if response.lower().strip() == "yes":
        return True
    else:
        return False
