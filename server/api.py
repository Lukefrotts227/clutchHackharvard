from flask import Flask, request, jsonify
from machinelearn import preprocess_input_data, predict_diabetes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    predictions = predict_diabetes(input_data)
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)