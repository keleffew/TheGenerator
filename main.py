from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-cat')
def get_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    return data[0]['url']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
