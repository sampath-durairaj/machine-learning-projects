from flask import Flask, request, jsonify

import util

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    total_sqft = float(request.form['total_sqft']) 
    location = float(request.form['location']) 
    bhk = float(request.form['bhk']) 
    bath = float(request.form['bath']) 
    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    return response

@app.route('/getlocations')
def get_location():
    response = jsonify({
        'locations' : util.getLocations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/')
def hello():
    return "Hello World!"
if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction")
    app.run(debug=True)