from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Carrega o modelo treinado
model = load_model('modelo_lstm_acao.h5')

# Inicializa o scaler (ajuste conforme seu treinamento)
scaler = MinMaxScaler()

@app.route('/predict', methods=['GET'])
def predict():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Converte para numpy array e ajusta formato
    input_data = np.array(data).reshape(-1, 1)
    input_scaled = scaler.fit_transform(input_data)  # Use o mesmo scaler do treinamento

    # Cria sequência para o modelo (ajuste seq_length conforme seu modelo)
    seq_length = model.input_shape[1]
    if len(input_scaled) < seq_length:
        return jsonify({'error': f'Input data must have at least {seq_length} values'}), 400

    X = input_scaled[-seq_length:].reshape(1, seq_length, 1)
    prediction_scaled = model.predict(X)
    prediction = scaler.inverse_transform(prediction_scaled)

    return jsonify({'prediction': float(prediction[0][0])})

@app.route('/health-check', methods=['POST'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)