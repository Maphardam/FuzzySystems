"""
Created on Dec 22, 2016.

@author: crekowski
"""
from collections import OrderedDict


class FuzzySet:
    """Fuzzy set class.

    A fuzzy set is an ordered dict. Each key represents a membership degree,
    whose range is defined by its value.

    Attributes:
        alphacuts: containers.OrderedDict containing alphacut values
    """

    def __init__(self):
        """Initialize set."""
        self.alphacuts = OrderedDict()

    def add_cuts_for_degree(self, degree, cuts):
        """Assign alpha cut range to degree.

        Args:
            degree: Membership degree (float)
            cuts: List of lists representing the ranges with the specified
                  degree
        """
        self.alphacuts[degree] = cuts

    def degrees(self):
        """Get alpha cut degrees.

        Returns:
            Alpha cut degree list
        """
        return self.alphacuts.keys()

    def iter_alphacuts(self):
        """Iterate alpha cuts.

        Returns:
            Iterator of alpha cut elements
        """
        return self.alphacuts.iteritems()

    def get_membership_value(self, x):
        """Get membership value for a value.

        Args:
            x: Float

        Returns:
            Membership value of x (float)
        """
        # Traverse alpha-cuts from high to low degrees of membership
        for degree, cuts in self.alphacuts.items():
            # Traverse all ranges for this degree
            for a, b in cuts:
                if a <= x and x <= b:
                    # x is located in this cut -> highest matching degree
                    return degree

        # No matching degree -> support is 0
        return 0.0


class FuzzySetOnCrisp:
    """FuzzySetOnCrisp class.

    A FuzzySetOnCrisp is a fuzzy set defined over a crip set.

    Attributes:
        memberships: Membership values for each element in the crisp set
    """

    def __init__(self, crisp_set):
        """Initialize FuzzySetOnCrisp.

        Args:
            crisp_set: Crisp set
        """
        self.memberships = OrderedDict()
        for el in crisp_set:
            self.memberships[el] = 0.0

    @property
    def crisp_set(self):
        """Get underlying crisp set.

        Returns:
            Underlying crisp set
        """
        return self.memberships.keys()

    def add_value_for_x(self, x, membership_value):
        """Set membership value for x.

        Args:
            x: Element of crisp set
            membership_value: Membership degree of x

        Raises:
            ValueError: The element is not contained in the fuzzy set.
        """
        if x in self.memberships:
            self.memberships[x] = membership_value
        else:
            raise ValueError("The given element {} is not contained in the" + \
                             " crisp set that this fuzzy set is defined on." \
                             .format(x))

    def get_membership_value(self, x):
        """Get membership value for a value.

        Args:
            x: Element of the underlying crisp set

        Returns:
            Membership value of x

        Raises:
            ValueError: The element is not contained in the fuzzy set.
        """
        if x in self.memberships:
            return self.memberships[x]
        else:
            raise ValueError("The given element {} is not contained in the" + \
                             " crisp set that this fuzzy set is defined on." \
                             .format(x))
