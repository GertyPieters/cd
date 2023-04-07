from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Als t werkt dan werkt t!</p>'

@app.route('/real')
def real():
    return '<p>En dan echt!</p>'

  
