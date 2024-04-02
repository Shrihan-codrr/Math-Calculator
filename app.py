from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def math_operations():
    equation = request.form['text']
    operation = request.form['operation']   
    
    api_url = ' https://newton.now.sh/api/v2//'+operation+'/'+equation
    requests.get(result).json()
    response = requests.get(api_url)
    answer = ['result']
    return render_template("index.html", result=answer , equation = equation)

if __name__ == "__main__":
    app.run()