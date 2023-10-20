from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/pyprocess', methods=['POST'])
def process_image():
    data = request.json
    file_path   = data['file_path']
    resultPath  = data['resultPath']
    processType = data['processType']

    cmd = "python3 processImage.py "+" "+  file_path  +" "+ resultPath +" "+ processType 
    print(cmd)
    os.system(cmd)
    response = {'result_file_path': resultPath}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

