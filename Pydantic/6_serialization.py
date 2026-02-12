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


# temp = Patient1.model_dump(include=['name', 'gender'])
# temp = Patient1.model_dump(exclude={'address': ['state']})
temp = Patient1.model_dump(exclude_unset={'address': ['state']})
# temp = Patient1.model_dump_json()

print(temp)
print(type(temp))

