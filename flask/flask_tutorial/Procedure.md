## Create virtual env
- Navigate to directory
- CTRL + SHIFT + P
- Search for "python interpreter"
- Select "Create virtual environment"

## Install flask
- pip install flask

## 
## Primitive way of running app
### Windows
- set FLASK_APP=appname.py
- flask --app appname run --debug
### Linux
- export FLASK_APP=appname.py
- flask --app appname run --debug
- --debug option allows hot reloading without having to shutdown server