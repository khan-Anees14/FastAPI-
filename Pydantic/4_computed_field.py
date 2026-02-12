from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


# pydantic model/class and by default all the fields are required
class Patient(BaseModel):

    name: str
    email: EmailStr 
    age: int    
    weight: float   # kg
    height: float   # mtr
    married: bool
    allergies: List[str]     
    contact_details: Dict[str, str]


    @computed_field
    @property
    def calculate_bmi(self) -> float:
            bmi = round(self.weight/(self.height**2),2)
            return bmi
    

def update_patient_data(patient: Patient):

            print(patient.name)
            print(patient.allergies)
            print(patient.married)
            print(patient.age)
            print('BMI', patient.calculate_bmi)
            print('updated')


patient_info = {'name': 'anish',
                'email': 'abc@hdfc.com',
                'linkedin_url': 'http://linkedin.com/12345',
                 'age': 30,
                   'weight': 75.2,
                   'height': 1.72,
                     'married':True,
                      'allergies':['pollen', 'dust'],
                       'contact_details':{'phone': '1234567', 'emergency': '987654321'} }

patient1 = Patient(**patient_info)


update_patient_data(patient1)
