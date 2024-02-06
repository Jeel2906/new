from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/post_data', methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = request.json  # Getting JSON data from the request
        print("Received data:", data)
        return jsonify(data)  # Returning the received JSON data as response

if _name_ == '_main_':
    app.run(debug=True)