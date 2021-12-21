import elems as el
import os
import json

nutrients_list = []

class Nutrient:
    def __init__(self,name,lcomposition):
        self.name = name
        self.lcomposition = lcomposition
        self.composition = [[],[]]

        for i in self.lcomposition.keys():
            val = (self.lcomposition.get(i))
            #key = el.elements_dic.get(i)  
            self.composition[0].append(i) #holds strings of element names
            self.composition[1].append(val) #holds percentage of elements
        
        print(self.composition)
        print(self.lcomposition)
        nutrients_list.append(self)

    def percentage(self,element):
        if element in self.composition[0]:
            indi = self.composition[0].index(element)
            return float(self.composition[1][indi])