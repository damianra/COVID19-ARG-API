from flask import jsonify
import pandas as pd
from flask_restful import Resource, reqparse
# Models
from sqlalchemy import and_

from models.models import Session, Argentina


class AllData(Resource):
    def get(self):
        # Open session in database
        session = Session()
        # Consult DB Argentina table and obtain all data
        argData = session.query(Argentina).all()
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in argData],
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class Date(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', help='This field cannot be blank', required=True)
        session = Session()
        date_ = parser.parse_args()
        arg = session.query(Argentina).filter(Argentina.date == date_['date'])
        session.close()
        return jsonify({
            'data': [result.serialized for result in arg],
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class DateRange(Resource):
    def get(self):
        # Object parser and create argument
        parser = reqparse.RequestParser()
        parser.add_argument('startdate', help='This field cannot be blank', required=True)
        parser.add_argument('enddate', help='This field cannot be blank', required=True)
        session = Session()
        data = parser.parse_args()
        startdate = data['startdate']
        enddate = data['enddate']
        arg = session.query(Argentina).filter(and_(
            Argentina.date >= startdate,
            Argentina.date <= enddate
        )).all()
        session.close()
        return jsonify({
            'data': [result.serialized for result in arg],
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class DatosProvincias(Resource):
    def get(self):
        html = pd.read_html('https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina')
        dataframe = pd.DataFrame(html[-1])
        dic = dataframe.to_dict()
        return jsonify(dic)
