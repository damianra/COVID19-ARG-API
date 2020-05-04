from datetime import datetime

from flask import jsonify
import pandas as pd
from flask_restful import Resource, reqparse


class EndData(Resource):
    def get(self):
        url = 'https://docs.google.com/spreadsheets/d/1U-dOOYAxHqFUOH1-w1uPSlce8pw_B79yDp0gEIBJJpM/export?format=csv'
        data = pd.read_csv(url)
        ultimafila = data.tail(1)
        lista = []
        for index, row in ultimafila.iterrows():
            lista.append({'fecha': row['Fecha'], 'casos': row['Casos'], 'muertes': row['Fallecidos'],
                           'recuperados': row['Recuperados'], 'terapia': row['Terapia']})
        # Return all data in JSON
        return jsonify({
            'data': lista,
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class AllData(Resource):
    def get(self):
        url = 'https://docs.google.com/spreadsheets/d/1U-dOOYAxHqFUOH1-w1uPSlce8pw_B79yDp0gEIBJJpM/export?format=csv'
        data = pd.read_csv(url)
        lista = []
        neg = None
        tot = None
        desc = None
        dailytestN = None
        for index, row in data.iterrows():
            if pd.isnull(row['Negativos']):
                neg = None
            else:
                neg = row['Negativos']

            if pd.isnull(row['Totales']):
                tot = None
            else:
                tot = row['Totales']

            if pd.isnull(row['Descartados por investigación epidemiológica']):
                desc = None
            else:
                desc = row['Descartados por investigación epidemiológica']

            if pd.isnull(row['Negativos']):
                dailytestN = None
            else:
                dailytestN = row['Negativos']
            lista.append(
                {
                    'date': row['Fecha'],
                    'cases': row['Casos'],
                    'deaths': row['Fallecidos'],
                    'recovered': row['Recuperados'],
                    'therapy': row['Terapia'],
                    'totalTestsNegative': neg,
                    'totalTests': tot,
                    'discardedNegative': desc,
                    'dailyTestNegative': dailytestN,
                    'dailyCases': row['Total positivos'],
                    'imported': row['Importados.1'],
                    'contactCase': row['Contacto estrecho / Conglomerado.1'],
                    'communityTransmission': row['Transmisión Comunitaria.1']
                }
            )

        return jsonify({
            'data': lista,
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class Date(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', help='This field cannot be blank', required=True)
        arg = parser.parse_args()
        url = 'https://docs.google.com/spreadsheets/d/1U-dOOYAxHqFUOH1-w1uPSlce8pw_B79yDp0gEIBJJpM/export?format=csv'
        data = pd.read_csv(url)
        fecha = datetime.strptime(arg['date'], '%Y-%m-%d')
        lista = []
        neg = None
        tot = None
        desc = None
        dailytestN = None
        for index, row in data.iterrows():
            if datetime.strptime(row['Fecha'], '%Y-%m-%d') == fecha:
                if pd.isnull(row['Negativos']):
                    neg = None
                else:
                    neg = row['Negativos']

                if pd.isnull(row['Totales']):
                    tot = None
                else:
                    tot = row['Totales']

                if pd.isnull(row['Descartados por investigación epidemiológica']):
                    desc = None
                else:
                    desc = row['Descartados por investigación epidemiológica']

                if pd.isnull(row['Tests negativos']):
                    dailytestN = None
                else:
                    dailytestN = row['Tests negativos']
                lista.append(
                    {
                        'date': row['Fecha'],
                        'cases': row['Casos'],
                        'deaths': row['Fallecidos'],
                        'recovered': row['Recuperados'],
                        'therapy': row['Terapia'],
                        'totalTestsNegative': neg,
                        'totalTests': tot,
                        'discardedNegative': desc,
                        'dailyTestNegative': dailytestN,
                        'dailyCases': row['Total positivos'],
                        'imported': row['Importados.1'],
                        'contactCase': row['Contacto estrecho / Conglomerado.1'],
                        'communityTransmission': row['Transmisión Comunitaria.1'],
                    }
                )
        return jsonify({
            'data': lista[0],
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class DateRange(Resource):
    def get(self):
        # Object parser and create argument
        parser = reqparse.RequestParser()
        parser.add_argument('startdate', help='This field cannot be blank', required=True)
        parser.add_argument('enddate', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        startdate = data['startdate']
        enddate = data['enddate']
        url = 'https://docs.google.com/spreadsheets/d/1U-dOOYAxHqFUOH1-w1uPSlce8pw_B79yDp0gEIBJJpM/export?format=csv'
        data = pd.read_csv(url)
        fechainicio = datetime.strptime(startdate, '%Y-%m-%d')
        fechafinal = datetime.strptime(enddate, '%Y-%m-%d')
        lista = []
        neg = None
        tot = None
        desc = None
        dailytestN = None
        for index, row in data.iterrows():
            if datetime.strptime(row['Fecha'], '%Y-%m-%d') >= fechainicio and datetime.strptime(row['Fecha'],'%d/%m/%Y') <= fechafinal:
                if pd.isnull(row['Negativos']):
                    neg = None
                else:
                    neg = row['Negativos']

                if pd.isnull(row['Totales']):
                    tot = None
                else:
                    tot = row['Totales']

                if pd.isnull(row['Descartados por investigación epidemiológica']):
                    desc = None
                else:
                    desc = row['Descartados por investigación epidemiológica']

                if pd.isnull(row['Tests negativos']):
                    dailytestN = None
                else:
                    dailytestN = row['Tests negativos']
                lista.append(
                    {
                        'date': row['Fecha'],
                        'cases': row['Casos'],
                        'deaths': row['Fallecidos'],
                        'recovered': row['Recuperados'],
                        'therapy': row['Terapia'],
                        'totalTestsNegative': neg,
                        'totalTests': tot,
                        'discardedNegative': desc,
                        'dailyTestNegative': dailytestN,
                        'dailyCases': row['Total positivos'],
                        'imported': row['Importados.1'],
                        'contactCase': row['Contacto estrecho / Conglomerado.1'],
                        'communityTransmission': row['Transmisión Comunitaria.1'],
                    }
                )
        return jsonify({
            'data': lista,
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class DatosWiki(Resource):
    def get(self):
        listaProvincias = []

        html = pd.read_html('https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina')
        dataframe = pd.DataFrame(html[-2])
        for index, row in dataframe.iloc[:-1].iterrows():
            listaProvincias.append(
                {'Provincia': row['Provincias'], 'Casos Confirmados': row['Casosconfirmados'], 'Muertes': row['Muertesconfirmadas'], 'Recuperados': row['Recuperacionesconfirmadas[n 1]\u200b'],
                 'Letalidad%': row['Letalidad %'],
                 'Poblacion2020': row['Población(proy. 2020)'], 'Prevalencia': row['Prevalencia(casos cada M de hab)']})

        return jsonify({'data': listaProvincias, 'disclaimer': 'Los datos son obtenidos desde Wikipedia'})


class CasosxProvincias(Resource):
    def get(self):
        urlprovincias = 'https://docs.google.com/spreadsheets/d/18yJBGAp5wVnJtQ7vg60J-eULbd64OzBvYHTdnxVgnr8/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA'
        data = pd.read_csv(urlprovincias)
        listaProvincia = []
        parser = reqparse.RequestParser()
        parser.add_argument('prov', help='This field cannot be blank', required=True)
        arg = parser.parse_args()
        prov = data.loc[:, 'province'] == arg['prov']
        df = data.loc[prov]

        for index, row in df.iterrows():
            listaProvincia.append(
                {
                    'Date': row['date'],
                    'Province': row['province'],
                    'Cases': row['cases'],
                    'Deaths': row['deaths']
                }
            )

        return jsonify({
            'data': listaProvincia,
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })


class DatosProvincias(Resource):
    def get(self):
        urlprovincias = 'https://docs.google.com/spreadsheets/d/18yJBGAp5wVnJtQ7vg60J-eULbd64OzBvYHTdnxVgnr8/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA'
        df = pd.read_csv(urlprovincias)
        listaProvincias = []
        for index, row in df.iterrows():
            listaProvincias.append(
                {
                    'Date': row['date'],
                    'Province': row['province'],
                    'Cases': row['cases'],
                    'Deaths': row['deaths']
                }
            )
        return jsonify({
            'data': listaProvincias,
            'disclaimer': 'Todos los datos fueron recolectados de los reportes diarios del ministerio de salud de Argentina https://www.argentina.gob.ar/coronavirus/informe-diario'
        })
