#simple web application using Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, Angeline!</p>'

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080)