from flask import Flask
from flask import request
from flask import json


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello World!'


# ‘/hooktest’ specifies which link will it work on
@app. route('/hooktest', methods=['POST'])
def hook_root():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200


if __name__ == '__main__':
    app.run(debug=True)
