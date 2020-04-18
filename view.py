from flask import jsonify

from flask_restful import Resource
# Models
from models import Session, Argentina


class AllData(Resource):
    def get(self):
        # Open session in database
        session = Session()
        # Consult DB Argentina table and obtain all data
        argData = session.query(Argentina).all()
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in argData]
        })