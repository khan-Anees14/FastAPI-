from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# pydantic model/class and by default all the fields are required
class Patient(BaseModel):

    # # ---------------- Type validation ------------------
    # name: str  
    # age: int    
    # weight: float
    # married: bool = False
    # allergies: Optional[List[str]] = None      # now it is optional field
    # contact_details: Dict[str, str]


    # ---------------- Data validation ------------------
    name: Annotated[str, Field(max_length=50, title='Name of the patient',
                                description='give the name of the patinet in less than 50 words',
                                examples=['nitish', 'anish'])]
    email: EmailStr                 # email validation
    linkedin_url: AnyUrl            # url validation
    age: int = Field(gt=0, lt=120) 

    weight: Annotated[float, Field(gt=0, strict=True)]     # data validation input>0
    
    married: Annotated[bool, Field(default=None, description='Is the patinet is married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]      # now it is optional field
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):

            print(patient.name)
            print(patient.age)
            print(patient.married)
            print('inserted into database')

def update_patient_data(patient: Patient):

            print(patient.name)
            print(patient.age)
            print('updated')
   

patient_info = {'name': 'nitish',
                'email': 'abc@gmail.com',
                'linkedin_url': 'http://linkedin.com/12345',
                 'age': 30,
                   'weight': 75.2,
                     'married':True,
                      'allergies':['pollen', 'dust'],
                       'contact_details':{'email':'abc@gmail.com', 'phone': '1234567'} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)