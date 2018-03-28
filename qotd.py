from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def display_qotd():
    r = requests.get('https://favqs.com/api/qotd')
    print r.json()
    return render_template('qotd.html', quote=r.json())