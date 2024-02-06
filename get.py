from flask import Flask

app = Flask(_name_)

@app.route('/get_name', methods=['GET'])
def get_name():
    name = "akshay"  # You can replace "John" with any name you want to return
    return {'name': name}

if _name_ == '_main_':
    app.run(debug=True)