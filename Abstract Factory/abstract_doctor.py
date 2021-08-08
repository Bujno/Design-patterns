from doctors.cardiologist_doctor import CardiologistDoctor
from doctors.internist_doctor import InternistDoctor
from doctors.orthopaedist_doctor import OrthopaedistDoctor

class UniversalDoctor:
    
    @staticmethod
    def get_specialist(sore_spot):
        if sore_spot == 'Heart':
            return CardiologistDoctor()
        elif sore_spot == 'Throat':
            return InternistDoctor()
        elif sore_spot == 'Leg':
            return OrthopaedistDoctor()
        else:
            return InternistDoctor()
    