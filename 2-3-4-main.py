from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# to load the json data from another file
def loadata():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data
    

@app.get('/')
def hello():
    return {'message': 'Patient Management System API'}

# 2nd get function
@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage you Patient records'}


# ----------------- To fetch the patients data ----------------------------
@app.get('/view')
def view():
     data = loadata()
     return data

# ---------------------- Path Parameter --------------------------------------------------------------
# specific patient retrieval, update, delete and with a correct HTTPException error
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description='ID of the patient in DB', example='P001')):  # path function enhances readability of input
    # load all the patient
    data = loadata()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail='Patient not found' )


# ------------------ sorting and ordering for a query --------------------------------------------------------------------------------------------------------------------
@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order' )):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = loadata()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data