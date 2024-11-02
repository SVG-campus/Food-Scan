from flask import Flask, request, jsonify, render_template
import os
from models.yolo import YOLOv5

app = Flask(__name__)

# Load the trained model
model = YOLOv5.load_from_checkpoint("model/best_model.ckpt")

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    # Save file temporarily
    file_path = f'temp/{file.filename}'
    file.save(file_path)

    # Predict
    results = model.predict(file_path)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
