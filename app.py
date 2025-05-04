from flask import Flask, request, render_template, flash, redirect, url_for
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# Check if Pillow is installed
try:
    from PIL import Image
except ImportError:
    raise ImportError("Pillow is not installed. Please install it using 'pip install Pillow'.")

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for flash messages
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load the pre-trained model
model = load_model('palm_oil_ripeness_model_finetuned.h5')
class_names = ['ripe', 'unripe', 'semiripe']

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_image(img_path):
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))
        return predicted_class, confidence
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        predicted_class, confidence = predict_image(file_path)
        if predicted_class:
            return render_template('result.html', filename=filename, prediction=predicted_class, confidence=confidence)
        else:
            flash(f'Error processing image: {confidence}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file format. Allowed formats: png, jpg, jpeg')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)