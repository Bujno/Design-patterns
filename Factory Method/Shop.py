from Bin import GlassBin
from random import choice
import Sweet
from inspect import getmembers, isclass

sweets = [getattr(Sweet, class_[0]) for class_ in getmembers(Sweet, isclass) if class_[1].__module__ == 'Sweet' and class_[0] != 'Sweet']

class Shop:
    
    def __init__(self, amount_of_bins):
        self.glass_bins = []
        for _ in range(amount_of_bins):
            type_ = choice(sweets)
            self.glass_bins.append(GlassBin(type_))
            
    def print_shop_info(self):
        for glass_bin in self.glass_bins:
            for element in glass_bin.set_of_sweets:
                print(type(element), end=" ")
            print()
            
    def fill(self):
        for glass_bin in self.glass_bins:
            for _ in range(glass_bin.limit):
                glass_bin.restock()
                
    def buy(self, how_many, type_):
        for glass_bin in self.glass_bins:
            if glass_bin.sweet_type == type_:
                while how_many and len(glass_bin.set_of_sweets) > 0:
                    how_many -= 1
                    glass_bin.get_sweet()
            
shop1 = Shop(10)
shop1.print_shop_info()    
    