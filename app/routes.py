from flask import render_template, request, jsonify
from app import app
from app.utils import preprocess_image
from app.model_loader import load_model_and_predict  # Change here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        image = preprocess_image(file)
        prediction = load_model_and_predict(image)
        return jsonify({'prediction': prediction})

    return jsonify({'error': 'Unknown error'})
