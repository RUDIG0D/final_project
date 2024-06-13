from flask import Flask, request
import joblib
import numpy

MODEL_PATH ='mlmodels1/model2.pkl'
SCALER_X_PATH ='mlmodels1/scaler_x2.pkl'
SCALER_Y_PATH ='mlmodels1/scaler_y2.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
sc_x = joblib.load(SCALER_X_PATH)
sc_y = joblib.load(SCALER_Y_PATH)

@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    floor = args.get('floor', default = -1, type=int)
    rooms = args.get('rooms', default = -1, type=int)
    area = args.get('area', default = -1, type=float)
    renovation = args.get('renovation', default = -1, type=int)

    x = numpy.array([rooms, area, floor, renovation]).reshape(1,-1)
    x = sc_x.transform(x)

    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1,-1))

    return str(result[0] [0])

if __name__ == '__main__':
    app.run(debug = True, port= 7776, host='0.0.0.0')
