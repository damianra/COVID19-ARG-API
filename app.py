from flask import Flask
from flask import render_template
from flask_restful import Api
from view import AllData

# Create flask application and API rest
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['JSON_SORT_KEYS'] = False
api = Api(app, prefix="/api/v1")


api.add_resource(AllData, '/alldata')


if __name__ == '__main__':

    app.run(debug=False)
