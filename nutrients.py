import elems as el
import os
import json

nutrients_list = []

class Nutrient:
    def __init__(self,name,lcomposition):
        self.name = name
        self.lcomposition = lcomposition
        self.composition = {}

        for i in self.lcomposition.keys():
            val = (self.lcomposition.get(i))
            #key = el.elements_dic.get(i)  
            self.composition[i]=val
        print(self.composition)
        print(self.lcomposition)
        nutrients_list.append(self)