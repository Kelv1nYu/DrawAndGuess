from flask import Flask
from flask_cors import CORS
from flask import render_template

app = Flask(__name__,
            static_url_path='/model',
            static_folder='model')

cors = CORS(app)


@app.route('/')
def index():
    return 'set up!'

if __name__ == '__main__':
    app.run()
