from flask import Flask, request, jsonify
import joblib
import numpy as np

MODEL_PATH = 'mlmodels/model.pkl'
SCALER_X_PATH = 'mlmodels/scaler_x.pkl'
SCALER_Y_PATH = 'mlmodels/scaler_y.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
sc_x = joblib.load(SCALER_X_PATH)
sc_y = joblib.load(SCALER_Y_PATH)

@app.route('/predict_price', methods=['GET'])
def predict_get():
    args = request.args
    open_plan = args.get('open_plan', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    renovation = args.get('renovation', default=-1, type=int)

    x = np.array([open_plan, rooms, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)

    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))

    return str(result[0][0])

@app.route('/predict_price', methods=['POST'])
def predict_post():
    data = request.get_json()

    open_plan = data.get('open_plan', -1)
    rooms = data.get('rooms', -1)
    area = data.get('area', -1.0)
    renovation = data.get('renovation', -1)

    if open_plan == -1 or rooms == -1 or area == -1.0 or renovation == -1:
        return jsonify({'error': 'Missing required parameter(s)'}), 400

    x = np.array([open_plan, rooms, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)

    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))

    return jsonify({'predicted_price': result[0][0]})

if __name__ == '__main__':
    app.run(debug=True, port=7778, host='0.0.0.0')