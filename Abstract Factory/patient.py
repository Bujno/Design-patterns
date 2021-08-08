from random import shuffle
from hospitals import NewAmsterdam, PrincetonPlainsboro

AVAILABLE_HOSPITALS = [NewAmsterdam, PrincetonPlainsboro]
shuffle(AVAILABLE_HOSPITALS)

class Patient:
    def __init__(self):
        self.names = ['Adam', 'Emilly', 'Evan', 'Lisa']
        self.ages = ['18', '6', '24', '63']
        self.sore_spots = ['Heart', 'Leg', 'Throat']
        self.diagnosis = None
    
    def request_diagnosis(self):
        shuffle(self.names)
        shuffle(self.ages)
        shuffle(self.sore_spots)
        request = {
            'name': self.names[0],
            'age': self.ages[0],
            'sore_spot': self.sore_spots[0]
        }
        chosen_hospital = AVAILABLE_HOSPITALS[0](request)
        self.diagnosis = chosen_hospital.get_specialist()
        
        
patient1 = Patient()
patient2 = Patient()
patient1.request_diagnosis()
patient2.request_diagnosis()
print(patient1.diagnosis)
print(patient2.diagnosis)