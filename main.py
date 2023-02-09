from  flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Test" 

@app.route('/route_added')
def route_added():
    return "Qadeer Hussain" 


if __name__ == "__main__":
    app.run(debug=True)

