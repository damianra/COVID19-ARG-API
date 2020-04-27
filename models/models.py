# coding: utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata
ENGINE = create_engine('mysql+pymysql://root:@127.0.0.1:3306/COVID19', echo=True)
Session = sessionmaker(bind=ENGINE)


# Model of argentina table
class Argentina(Base):
    __tablename__ = 'argentina'

    date = Column(String(150), primary_key=True)
    cases = Column(INTEGER(11), nullable=False)
    deaths = Column(INTEGER(11), nullable=False)
    recovered = Column(INTEGER(11), nullable=False)
    terapy = Column(INTEGER(11), nullable=False)
    testsNegative = Column(INTEGER(11), nullable=False)
    tests = Column(INTEGER(11), nullable=False)
    discardedNegatives = Column(INTEGER(11), nullable=False)
    dailyTestNegative = Column(INTEGER(11), nullable=False)
    dailyCases = Column(INTEGER(11), nullable=False)
    imported = Column(INTEGER(11), nullable=False)
    contactCase = Column(INTEGER(11), nullable=False)
    communitary_Transmission = Column('communitary Transmission', INTEGER(11), nullable=False)

    # Property serialized return consult in dictionary
    @property
    def serialized(self):
        return {
            'date': self.date,
            'cases': self.cases,
            'deaths': self.deaths,
            'recovered': self.recovered,
            'therapy': self.terapy,
            'testsNegative': self.testsNegative,
            'tests': self.tests,
            'discardedNegatives': self.discardedNegatives,
            'dailyTestNegative': self.dailyTestNegative,
            'dailyCases': self.dailyCases,
            'imported': self.imported,
            'contactCase': self.contactCase,
            'communityTransmission': self.communitary_Transmission
        }
        
    
        
class Provincia(Base):
    __tablename__ = 'provincias'

    id = Column(INTEGER(11), primary_key=True)
    fecha = Column(String(100), nullable=False)
    provincia = Column(String(200), nullable=False)
    casos = Column(INTEGER(11), nullable=False)
    muertes = Column(INTEGER(11), nullable=False)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'date': self.fecha,
            'province': self.provincia,
            'cases': self.casos,
            'deaths': self.muertes
        }



class User(Base):
    __tablename__ = 'users'

    UserID = Column(INTEGER(11), primary_key=True)
    Name = Column(String(30), nullable=False, unique=True)
    _pass = Column('pass', String(50), nullable=False)
