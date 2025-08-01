import pickle
import json
import numpy as np
import pandas as pd

__location = None
__columns = None
__model = None

def get_house_price(bhk, bath, sqft, age, bal, location):
    try:
        location_index = __columns.index(location.lower())
    except:
        location_index = -1

    formatted_age = pd.cut([age], bins=[-1,5,10,20], labels=['New','Mid New','Mid'])[0]

    age_index = __columns.index(formatted_age.lower())

    features = np.zeros(len(__columns))

    features[0] = bhk
    features[1] = bath
    features[2] = sqft
    features[3] = bal

    if location_index >= 0:
        features[location_index] = 1

    if age_index >= 0:
        features[age_index] = 1

    prediction = __model.predict([features])
    return round(prediction[0],2)


def load_saved_artifacts():

    global __columns
    global __model
    global __location

    with open('../common/columns_city.json', 'r') as f:
        __columns = json.load(f)['columns']
        __location = __columns[5:]
        print("Columns loaded successfully", __columns)
        
    global __model
    if __model is None:
        with open('../artifacts/house_predictor_citykol.pkl', 'rb') as f:
            __model = pickle.load(f)

    print("Artifacts loaded successfully")

def get_location_names():
    return __location

def get_columns():
    return __columns

