import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x= np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1
    
    print([x])
    return round(__model.predict([x])[0],2)


def getLocations():
    print(__locations)
    load_saved_artificats()
    return __locations 


def load_saved_artificats():
    print('locading')
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open("./artifacts/house_price_model", "rb") as f:
        __model = pickle.load(f)

if __name__=='__main__':
    load_saved_artificats()
    print(getLocations())
    print(get_estimated_price('2nd Phase Judicial Layout', 1000,2,2))
