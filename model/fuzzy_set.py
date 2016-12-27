'''
Created on Dec 22, 2016

@author: crekowski
'''
from collections import OrderedDict


class FuzzySet:
    
    def __init__(self):
        self.alphacuts = OrderedDict()
    
    def add_cuts_for_degree(self, degree, cuts):
        self.alphacuts[degree] = cuts
    
    def degrees(self):
        return self.alphacuts.keys()
    
    def iter_alphacuts(self):
        return self.alphacuts.iteritems()
    
    def get_membership_value(self, x):
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
    
    def __init__(self, crisp_set):
        self.memberships = {x: 0.0 for x in crisp_set}
    
    @property
    def crisp_set(self):
        return self.memberships.keys()
    
    def add_value_for_x(self, x, membership_value):
        if x in self.memberships:
            self.memberships[x] = membership_value
        else:
            raise ValueError("The given element {} is not contained in the " + \
                             "crisp set that this fuzzy set is defined on." \
                             .format(x))
    
    def get_membership_value(self, x):
        if x in self.memberships:
            return self.memberships[x]
        else:
            raise ValueError("The given element {} is not contained in the " + \
                             "crisp set that this fuzzy set is defined on." \
                             .format(x))
