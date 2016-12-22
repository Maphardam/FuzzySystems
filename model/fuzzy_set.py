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
