from flask import Flask
from flask import render_template
from flask_restful import Api
from view import AllData, Date, DateRange

# Create flask application and API rest
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'
app.config['JSON_SORT_KEYS'] = False
api = Api(app, prefix="/api/v1")


api.add_resource(AllData, '/alldata')
api.add_resource(Date, '/date')
api.add_resource(DateRange, '/range')

if __name__ == '__main__':

    app.run(debug=False)
