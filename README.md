## Digit-Recognition

This project implements a web-based digit recognition system using a Convolutional Neural Network (CNN) to classify hand-drawn digits. The frontend provides a canvas where users can draw a digit, and the backend, powered by a Python-based AI model in a Jupyter environment, processes the drawing and predicts the digit.

Project Structure

Frontend: Built with JavaScript, featuring a simple canvas element for drawing digits. The drawing is sent to the backend for recognition.
Backend: Developed using Jupyter Notebook and Python. It utilizes a trained CNN model to recognize handwritten digits and return predictions.
Features

Canvas for Drawing: Users can draw a digit (0-9) on a canvas using their mouse or touch input.
Real-time Recognition: The drawn digit is captured as an image and sent to the backend for processing.
AI-based Prediction: The backend uses a pre-trained CNN model to analyze the image and predict the digit with high accuracy.
Feedback Display: The predicted digit is displayed on the frontend.
Requirements

Frontend: HTML, CSS, JavaScript
Backend: Python, Jupyter Notebook, TensorFlow/Keras for model processing
Setup

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/Digit-Recognition.git
cd Digit-Recognition
Backend Setup:
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Launch the Jupyter Notebook server and run the backend model.
Frontend Setup:
Open index.html in a web browser.
Usage

Draw a digit on the canvas provided.
Press the "Recognize" button to send the drawing to the backend.
The backend processes the image and returns the recognized digit, displayed on the screen.
Model Training

The CNN model was trained on the MNIST dataset, containing thousands of labeled handwritten digits. You can find the training code in the notebooks folder.

Future Improvements

Improve the accuracy of digit recognition.
Add error-handling and feedback for unrecognized inputs.
Implement further frontend enhancements for better user interaction.

