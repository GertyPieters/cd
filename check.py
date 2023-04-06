from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Als t werkt dan werkt t!'

@app.route('/real')
def real():
    return 'En dan echt!'

  
