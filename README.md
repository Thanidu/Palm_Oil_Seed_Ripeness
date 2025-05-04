# Palm Oil Ripeness Detection Web App

This is a Flask-based web application that uses a pre-trained Convolutional Neural Network (CNN) model to predict the ripeness of palm oil fruits from uploaded images. The model classifies images into three categories: **ripe**, **unripe**, and **semiripe**.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Model Details](#model-details)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Features
- Upload images (PNG, JPG, JPEG) to predict palm oil ripeness.
- Displays the predicted class (ripe, unripe, semiripe) and confidence score.
- User-friendly interface styled with Tailwind CSS.
- Error handling for invalid file formats and image processing issues.

## Project Structure
```
palm-oil-ripeness-app/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── palm_oil_ripeness_model_finetuned.h5  # Pre-trained CNN model (optional, not in repo)
├── static/
│   └── uploads/               # Directory for uploaded images
├── templates/
│   ├── index.html             # Home page with upload form
│   └── result.html            # Prediction result page
└── README.md                  # Project documentation
```

## Prerequisites
- Python 3.9–3.11
- Git
- A web browser (e.g., Chrome, Firefox)
- (Optional) Virtual environment for dependency isolation

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Thanidu/Palm_Oil_Seed_Ripeness.git
   cd Palm_Oil_Seed_Ripeness
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain the Pre-trained Model**:
   - The `palm_oil_ripeness_model_finetuned.h5` file is not included in the repository due to its size.
   - Download the model from [https://drive.google.com/file/d/1dhVfe5fsF9xcpyuI-OYf-3Sn-0osJN8p/view?usp=sharing] and place it in the project root directory.

## Running the Application
1. Ensure the model file (`palm_oil_ripeness_model_finetuned.h5`) is in the project root.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open a web browser and navigate to `http://127.0.0.1:5000`.

## Usage
1. On the home page, click "Choose File" to select a palm oil fruit image (PNG, JPG, or JPEG).
2. Click "Predict" to upload the image.
3. View the prediction result, which includes:
   - The uploaded image.
   - The predicted ripeness class (ripe, unripe, or semiripe).
   - The confidence score (as a percentage).
4. Click "Upload Another Image" to try another image.

## Model Details
- **Framework**: TensorFlow Keras
- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: Images resized to 224x224 pixels
- **Output**: Classification into three classes: ripe, unripe, semiripe
- **Training Data**: Not included in this repository (assumed to be pre-trained)

## Notes
- **Model File**: The `.h5` model file is large and not tracked in Git. Use Git LFS or a cloud storage service to share it.
- **Dependencies**: Ensure all dependencies in `requirements.txt` are installed. If issues arise, check for version compatibility (e.g., TensorFlow requires Python 3.9–3.11).
- **Error Handling**: The app handles invalid file formats and image processing errors, displaying messages via Flask's flash system.
- **Styling**: The app uses Tailwind CSS via CDN for a responsive UI.
- **Deployment**: For production, consider using a WSGI server (e.g., Gunicorn) and a reverse proxy (e.g., Nginx). Do not use `app.run(debug=True)` in production.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows PEP 8 guidelines and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
