from Sweet import Sweet


class GlassBin:
    def __init__(self, sweet_type: Sweet):
        self.sweet_type = sweet_type
        self.limit = 100
        self.minimum = 10
        self.set_of_sweets = {self.sweet_type.create_sweet() for _ in range(10)}
        
    def restock(self):
        if len(self.set_of_sweets) >= self.minimum:
            return 
        self.set_of_sweets.add(self.sweet_type.create_sweet())
        
    def get_sweet(self):
        return self.set_of_sweets.pop()