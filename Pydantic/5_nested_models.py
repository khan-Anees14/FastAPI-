from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address       # nested models/class

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1  = Address(**address_dict)

Patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

Patient1 = Patient(**Patient_dict)

print(Patient1)
print(Patient1.name)
print(Patient1.address.city)
print(Patient1.address.pin)


# What we will get using the Nested models

# 1. Better organization of related data (e.g. vitals, address, insurance)

# 2. Reusability: Use Vitals in multiple models (e.g. Patient, MedicalRecord)

# 3. Readability: Easier for developers and API consumers to understand

# 4. Validation: Nested models are validated automatically no extra work needed