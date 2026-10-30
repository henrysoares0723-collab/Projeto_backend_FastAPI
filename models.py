from sqlalchemy import create_engine
from sqlalchemy import declaretive_base

#Criação de banco de dados 
db = create_engine("sqllite:///banco.db")

#Criação da base do banco de dados 
base = declaretive_base()