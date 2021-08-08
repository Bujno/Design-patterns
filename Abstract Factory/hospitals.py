from abstract_hospital import Hospital

class NewAmsterdam(Hospital):
    pass
    
class PrincetonPlainsboro(Hospital):
    
    @staticmethod
    def make_a_call():
        print("We found specialist for U in Princeton Plainsboro!")
    
    def get_specialist(self):
        a_doctor = super().get_specialist()
        self.make_a_call()
        return a_doctor
    