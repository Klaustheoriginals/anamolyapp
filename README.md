# Anamoly App

A Python-based web application for identifying anomalies in datasets using machine learning techniques.

## Project Structure

- app.py – Main application logic and routing.
- templates/ – HTML templates for rendering the UI.
- static/ – Contains images, plots, CSS files, and other static assets.
- uploads/ – Folder to store uploaded datasets and generated files.
- requirements.txt – List of dependencies required for the project.

## Features

- Upload dataset files and perform anomaly detection.
- Visualize results with charts and plots.
- Download generated reports and images.
- Interactive user interface built with Flask and Bootstrap.

## Installation

1. Clone the repository:
   git clone https://github.com/Klaustheoriginals/anamolyapp.git
   cd anamolyapp

2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv/bin/activate # macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Open `http://127.0.0.1:5000/` in your browser.

## Usage

1. Upload your dataset file (CSV format recommended).
2. Choose anomaly detection options.
3. View the generated plots and predictions.
4. Download reports as needed.

## Dependencies

- Flask
- NumPy
- Pandas
- scikit-learn
- Matplotlib
- Other libraries listed in requirements.txt

## Notes

- Ensure Python 3.6+ is installed.
- Use a virtual environment to avoid conflicts with system packages.
- Always review uploaded files for security.

## Contributing

Feel free to fork the repository, create issues, or submit pull requests. Contributions are welcome!





