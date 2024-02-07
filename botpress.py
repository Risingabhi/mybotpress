from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        print("yes request is coming")
        lead_data = request.json
        print("Data received:", lead_data)
        return 'Data received successfully!', 200
    else:
        return 'Invalid request method', 405

if __name__ == '__main__':
    app.run(port=10000,debug=True)
