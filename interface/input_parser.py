"""
Created on Dec 22, 2016.

@author: crekowski
"""


def read_number_list(input_string):
    """Parse string to list of floats.

    Args:
        input_string: String

    Returns:
        A list of floats.
    """
    try:
        # Split list by ','
        return [float(s.strip()) for s in input_string.split(',')]
    except ValueError:
        # Something was not a float in there
        return None


def read_list(input_string):
    """Parse string to list.

    Args:
        input_string: String

    Returns:
        A list.
    """
    return [s.strip() for s in input_string.split(',') if s.strip()]


def read_membership_value(mv_string):
    """Parse string to float and verify as valid membership value.

    Args:
        mv_string: String

    Returns:
        Float value (if valid membership value), or None.
    """
    try:
        v = float(mv_string)
    except ValueError:
        # That was not a float
        return None

    if v >= 0.0 and v <= 1.0:
        return v
    else:
        # This is not a valid membership degree
        return None


def read_cut_values(cut_string):
    """Parse string to float list and verify as valid alpha cut.

    Args:
        cut_string: String

    Returns:
        A list of floats (if valid alpha cut), or None.
    """
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
    """Parse string to float.

    Args:
        x_string: String

    Returns:
        Float, if possible to parse, or None.
    """
    try:
        return float(x_string.strip())
    except ValueError:
        return None
