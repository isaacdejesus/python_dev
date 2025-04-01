## Create virtual env
- Navigate to directory
- CTRL + SHIFT + P
- Search for "python interpreter"
- Select "Create virtual environment"

## Install flask
- pip install flask

## A basic flask app
- A flask app can be as simple as a single file: see hello.py
```python
# Flask app can be a single file
# run it: flask --app filename run --debug
# flask --app hello run --debug
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello, world'
 ```