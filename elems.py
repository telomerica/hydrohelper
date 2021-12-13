elements_ls = []
elements_ls1 = []
elements_dic = {}
class Element:
    def __init__(self,name,mmass):
        self.name = name
        self.mmass = mmass
        elements_dic[self.name]=self
        elements_ls.append(self)
        elements_ls1.append(self.name)

N = Element("N",14.01)
P = Element("P",30.97)
K = Element("K",39.09)
Mg = Element("Mg",24.3)
Ca = Element("Ca",40.07)
S = Element("S",32.06)
Cl = Element("Cl",35.45)
Fe = Element("Fe",55.85)
Zn = Element("Zn",65.39)
Mn = Element("Mn",54.94)
B = Element("B",10.81)
Cu = Element("Cu",63.55)
Mo = Element("Mo",95.94)