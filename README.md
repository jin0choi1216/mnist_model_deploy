# Image Classification Model

This is a simple Flask web application for image classification using a TensorFlow model. It allows users to upload images and get predictions from the trained model.

## Project Structure

- `app/`: Contains the Flask application files.
  - `static/`: Static files such as stylesheets and images.
  - `templates/`: HTML templates for rendering web pages.
  - `__init__.py`: Initializes the Flask app.
  - `routes.py`: Defines URL routes and view functions.
  - `utils.py`: Provides utility functions for image preprocessing.
  - `model_loader.py`: Loads the trained TensorFlow model and performs predictions.

- `models/`: Contains saved model files.
  - `your_model.h5`: Example saved model file.

- `modeling.ipynb`: Jupyter Notebook for creating and training the TensorFlow model.

- `run.py`: Entry point for running the Flask app.

- `config.py`: Configuration settings for the project.

- `requirements.txt`: Lists required Python packages for the project.

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/your-username/your-project.git
   ```

2. Navigate to the project directory:
   ```
   cd your-project
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```
   python run.py
   ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to access the app.

## Usage
- Upload an image using the provided form.
- Click the "Predict" button to get a prediction from the trained model.
- The predicted class or label will be displayed on the web page.



