from abc import ABC
from random import choice


class Sweet(ABC):
    
    @classmethod
    def create_sweet(cls, *args, **kwargs):
        raise Exception("Sorry, you can't")
    
    
class Jawbreaker(Sweet):
    
    @classmethod
    def create_sweet(cls):
        return Jawbreaker()
    
    
class Gummy(Sweet):
    colors = ['red', 'green', 'blue']
    shapes = ['bear', 'giraffe', 'elephant']
    
    def __init__(self, color, shape):
        if color is not None:
            self.color = color
        else:
            self.color = choice(Gummy.colors)
        if shape is not None:
            self.shape = shape
        else:
            self.shape = choice(Gummy.shapes)
    
    @classmethod
    def create_sweet(cls, color=None, shape=None):
        return Gummy(color, shape)
    
    
class Fudge(Sweet):
    ings = ['Without', 'With chocolate']
    
    def __init__(self, extra_ingredient):
        if extra_ingredient is not None:
            self.extra_ingredient = extra_ingredient
        else:
            self.extra_ingredient = choice(Fudge.ings)
            
    @classmethod
    def create_sweet(cls, extra_ingredient=None):
        return Fudge(extra_ingredient)
    

class BoiledSweet(Sweet):
    colors = ['red', 'green', 'blue']
    
    def __init__(self, color=None):
        if color is not None:
            self.color = color
        else:
            self.color = choice(BoiledSweet.colors)
    
    @classmethod
    def create_sweet(cls, color=None):
        return BoiledSweet(color)