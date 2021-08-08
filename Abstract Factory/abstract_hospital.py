from abstract_doctor import UniversalDoctor

class Hospital:
    def __init__(self, patient_request: dict):
        self.patient_request = patient_request
        
    def get_specialist(self):
        doctor = UniversalDoctor.get_specialist(self.patient_request['sore_spot'])
        return doctor.get_diagnosis()
    