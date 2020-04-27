# Encrypt library
import bcrypt
import pandas as pd
from sqlalchemy import and_

from models.models import Session, User, Argentina
semilla = bcrypt.gensalt()


def log(user, passw):
    session = Session()
    usr = session.query(User).filter(User.Name == user).first()
    session.close()
    ret = None
    if usr:
        password = usr._pass.encode('utf-8')
        if bcrypt.checkpw(passw, password):
            ret = True
        else:
            ret = False
        return ret


def newdata(dic):
    session = Session()
    ndata = Argentina(date=dic['date'], cases=dic['casos'], deaths=dic['muertes'], recovered=dic['recuperados'],
                      terapy=dic['terapia'],
                      testsNegative=dic['testsNegatives'], tests=dic['tests'],
                      discardedNegatives=dic['negativosDescarte'],
                      dailyCases=dic['casosDiarios'], dailyTestNegative=dic['testNegativosDiarios'],
                      imported=dic['casosImportados'],
                      contactCase=dic['contactoEstrecho'], communitary_Transmission=dic['trasmisionComunitaria'])
    session.add(ndata)
    session.commit()
    session.flush()
    session.close()


def ultimodato():
    session = Session()
    udato = session.query(Argentina).order_by(Argentina.date.desc()).first()
    session.close()
    return udato


def updatedata(dic, id):
    session = Session()
    session.query(Argentina).filter(Argentina.date == id).update(dic)
    session.commit()
    session.flush()
    session.close()


def deleteCase(id):
    session = Session()
    session.query(Argentina).filter(Argentina.date == id).delete()
    session.commit()
    session.flush()
    session.close()


def edit(id):
    session = Session()
    case = session.query(Argentina).filter(Argentina.date == id).first()
    session.close()
    return case


def lista():
    session = Session()
    cases = session.query(Argentina).all()
    session.close()
    return cases


def listaProvincias():
    listaprovincias = []

    html = pd.read_html('https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina')
    dataframe = pd.DataFrame(html[-1])
    for index, row in dataframe.iloc[:-1].iterrows():
        listaprovincias.append(
            {'Provincia': row['Provincias'], 'Casos Confirmados': row['Casosconfirmados'],
             'Muertes': row['Muertesconfirmadas'], 'Recuperados': row['Recuperacionesconfirmadas[n 1]\u200b'],
             'Letalidad%': row['Letalidad %'],
             'Poblacion2020': row['Población(proy. 2020)'], 'Prevalencia': row['Prevalencia(casos cada M de hab)']})
    return listaprovincias


def listaData():
    session = Session()
    # Consult DB Argentina table and obtain all data
    argData = session.query(Argentina).all()
    session.close()
    data = [result.serialized for result in argData]
    return data
