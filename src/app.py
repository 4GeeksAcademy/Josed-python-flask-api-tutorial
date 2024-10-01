from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "done": True, "label": "Sample Todo 1" },
    { "done": True, "label": "Sample Todo 2" }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)  
        return jsonify(todos), 200
    else:
        return jsonify({"error": "No existe ese Todo"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)