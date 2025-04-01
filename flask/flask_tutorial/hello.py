# Flask app can be a single file
# run it: flask --app filename run --debug
# flask --app hello run --debug
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello, world'