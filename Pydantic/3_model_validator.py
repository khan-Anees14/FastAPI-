from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


# pydantic model/class and by default all the fields are required
class Patient(BaseModel):

    name: str
    email: EmailStr 
    age: int    
    weight: float
    married: bool
    allergies: List[str]      
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model
    

    
def update_patient_data(patient: Patient):

            print(patient.name)
            print(patient.allergies)
            print(patient.age)
            print('updated')




patient_info = {'name': 'nitish',
                'email': 'abc@hdfc.com',
                'linkedin_url': 'http://linkedin.com/12345',
                 'age': 30,
                   'weight': 75.2,
                     'married':True,
                      'allergies':['pollen', 'dust'],
                       'contact_details':{'phone': '1234567', 'emergency': '987654321'} }

patient1 = Patient(**patient_info)

update_patient_data(patient1)