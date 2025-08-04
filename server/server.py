from flask import Flask, request, jsonify, send_from_directory
import util

app = Flask(__name__, static_folder='../UI', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'app.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
