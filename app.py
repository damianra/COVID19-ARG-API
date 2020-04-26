from flask import Flask, request, session, flash
from flask import render_template
from flask_restful import Api
from views.api import AllData, Date, DateRange, DatosProvincias
from views.web import log, newdata, ultimodato, deleteCase, updatedata, lista, edit
from flask_cors import CORS

# Create flask application and API rest
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['JSON_SORT_KEYS'] = False
api = Api(app, prefix="/api/v1")

api.add_resource(AllData, '/alldata')
api.add_resource(Date, '/date')
api.add_resource(DateRange, '/range')
api.add_resource(DatosProvincias, '/provinces')


@app.route('/')
@app.route('/index')
def index():
    ud = ultimodato()

    dic = {'fecha': ud.date, 'casos': ud.cases, 'muertes': ud.deaths, 'recuperados': ud.recovered}

    return render_template('plantilla.html', ud=dic)


@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    passw = request.form['pass'].encode('utf-8')
    validation = log(user, passw)
    if validation:
        session['logged_in'] = True
        return dashboard()
    else:
        flash('Usuario y/o contraseño incorrectos')
        return formulario()


@app.route('/form')
def formulario():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if session['logged_in']:
        return render_template('dashboard.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    if session['logged_in']:
        session['logged_in'] = False
    return render_template('login.html')


@app.route('/insert', methods=['POST'])
def insert():
    date = request.form['fecha']
    casos = request.form['casos']
    muertes = request.form['muertes']
    recuperados = request.form['recuperados']
    terapia = request.form['terapia']
    testsNegatives = request.form['testsNegatives']
    tests = request.form['tests']
    negativosDescarte = request.form['negativosDescarte']
    casosDiarios = request.form['casosDiarios']
    testNegativosDiarios = request.form['testNegativosDiarios']
    casosImportados = request.form['CasosImportados']
    contactoEstrecho = request.form['contactoEstrecho']
    trasmisionComunitaria = request.form['trasmisionComunitaria']

    dicCasos = {'date': date,
                'casos': casos,
                'muertes': muertes,
                'recuperados': recuperados,
                'terapia': terapia,
                'testsNegatives': testsNegatives,
                'tests': tests,
                'negativosDescarte': negativosDescarte,
                'casosDiarios': casosDiarios,
                'testNegativosDiarios': testNegativosDiarios,
                'casosImportados': casosImportados,
                'contactoEstrecho': contactoEstrecho,
                'trasmisionComunitaria': trasmisionComunitaria}
    try:
        newdata(dicCasos)
        return dashboard()
    except ValueError:
        return "FAIL"


@app.route('/documentacion')
def documentacion():
    return render_template('documentation.html')


@app.route('/delete/<string:id>')
def delete(id):
    deleteCase(id)
    flash('Caso eliminado Correctamente')
    return list()


@app.route('/edit/<string:id>')
def getCase(id):
    case = edit(id)
    print(case)
    return render_template('dashboardedit.html', case=case)


@app.route('/list')
def list():
    if session['logged_in']:
        cases = lista()
        return render_template('list.html', cases=cases)
    else:
        return render_template('login.html')


@app.route('/update', methods=['POST'])
def update():
    date = request.form['fecha']
    casos = request.form['casos']
    muertes = request.form['muertes']
    recuperados = request.form['recuperados']
    terapia = request.form['terapia']
    testsNegatives = request.form['testsNegatives']
    tests = request.form['tests']
    negativosDescarte = request.form['negativosDescarte']
    casosDiarios = request.form['casosDiarios']
    testNegativosDiarios = request.form['testNegativosDiarios']
    casosImportados = request.form['CasosImportados']
    contactoEstrecho = request.form['contactoEstrecho']
    trasmisionComunitaria = request.form['trasmisionComunitaria']

    dicCasos = {'date': date,
                'cases': casos,
                'deaths': muertes,
                'recovered': recuperados,
                'terapy': terapia,
                'testsNegative': testsNegatives,
                'tests': tests,
                'discardedNegatives': negativosDescarte,
                'dailyCases': casosDiarios,
                'dailyTestNegative': testNegativosDiarios,
                'imported': casosImportados,
                'contactCase': contactoEstrecho,
                'communitary_Transmission': trasmisionComunitaria}
    try:
        updatedata(dicCasos, date)
        flash('Modificado Correctamente')

        return list()

    except ValueError:
        return "FAIL"


if __name__ == '__main__':
    app.run(debug=False)
