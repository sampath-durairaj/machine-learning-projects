from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('RandomForest.pk1','rb') as file:
    newmodel = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    corridor = request.form['corridor']
    speed = float(request.form['speed'])
    volume = float(request.form['VOLUME'])
    occupancy = float(request.form['occupancy'])
    td = float(request.form['td'])

    reshaped_data = np.array([corridor,speed,volume,occupancy,td]).reshape(1,-1)
    prediction = newmodel.predict(reshaped_data)
    return render_template('index.html', prediction=prediction[0],
corridor=corridor,
                       speed=speed,
                       volume=volume,
                       occupancy=occupancy,
                       td=td
)

if __name__ == '__main__':
    app.run(debug=True)