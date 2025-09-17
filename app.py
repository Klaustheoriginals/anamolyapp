from flask import Flask, render_template, request, send_file, url_for
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create folders if not exist
for folder in [UPLOAD_FOLDER, STATIC_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)
    data = df.copy()

    if 'label' in data.columns:
        data.drop(columns=['label'], inplace=True)

    # Isolation Forest
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    predictions = model.predict(data)
    scores = model.decision_function(data)

    df['anomaly'] = predictions
    df['anomaly_score'] = scores

    # Save predicted CSV
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'predicted_output.csv')
    df.to_csv(result_path, index=False)

    # Plot 1: Pie chart
    pie_path = os.path.join('static', 'anomaly_pie.png')
    counts = df['anomaly'].value_counts()
    labels = ['Normal' if x == 1 else 'Anomaly' for x in counts.index]
    plt.figure()
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.savefig(pie_path)
    plt.close()

    # Plot 2: Anomaly score histogram
    score_path = os.path.join('static', 'score_hist.png')
    plt.figure()
    sns.histplot(scores, kde=True, bins=50)
    plt.title("Anomaly Score Distribution")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Frequency")
    plt.savefig(score_path)
    plt.close()

    return render_template('result.html',
                           anomaly_count=int((df['anomaly'] == -1).sum()),
                           normal_count=int((df['anomaly'] == 1).sum()),
                           pie_path=url_for('static', filename='anomaly_pie.png'),
                           score_path=url_for('static', filename='score_hist.png'))


@app.route('/download')
def download():
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'predicted_output.csv')
    return send_file(result_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
