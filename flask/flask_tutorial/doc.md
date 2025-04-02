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
app = Flask(__name__)  # flask instance
@app.route('/')
def hello():
    return 'hello, world'
 ```
 ## Project structure
 - Bigger projects use *packages* to organize code into smaller modules. Project directory becomes:
    - *flaskr/*: python package containing app code and files
    - *tests/*: contains test modules
    - *.venv/*: virtual env where flask and other dependencies are installed
- A flask app is an instance of Flask class. Everything about app such as config and URLs are registered with class.
- In *hello.py* the flask instance is created globally at the top of the file
- Proper way to create flask instance is inside a function with config, registration and any other set up needed by
  app taking place inside the function which will return the app.
### Creating a package
- Create a folder with desired package name. In this case *flasker*
- Create *__init__.py* in it with app factory function/function that returns the app
```python
# flask_tutorial/flasker/__init__.py
import os
from flask import Flask
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
- *create_app*: is the app factory function. It does the following:
    - *app = Flask(__name__, instance_relative_config=True): creates the Flask instance
        - *__name__* is the name of current python module. 
        - *instance_relative_config=True*, tells app that config files are relative to *instance folder* which is 
           located outside of *flaskr* package and can hold local data that isn't committed to version control, such
           as config secrets and database file.
    - *app.config.from_mapping()*: sets default config used by app
        - *SECRET_KEY*, used to keep data safe. Set to 'dev' to provide a convenient val during dev but should be set to
           random val for deployment.
        - *DATABASE*, is path where SQLite database file will be saved. It's under *app.instance_path* which is path 
           Flask has chosen for instance folder.
    - *app.config.from_pyfile()*: Overrides default config with info from config.py in instance folder, if it exists. For
       ex, it can be used to set a real *SECRET_KEY* during deployment.
        - *test_config* can be passed to factory func to be used instead of instance config. So tests ran during tutorial
           can be config independtently of dev values
    - *os.makedirs()*: ensures *app.instance_path* exists bc it isn't automatically created by Flask but it is needed since
       that's where SQLite database file will be created. 
    - *@app.route()*: creates a simple route to check that app is working. 
### Running app
- In main project dir: /flask_tutorial
```python
flask --app flaskr run --debug
```
- Where flaskr is the name of the package just created.
