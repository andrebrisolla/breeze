from flask import Flask
import sys,os

from lib.db import Db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Teste DB
@app.route('/db')
def db():
    try:
        Db('change').select('insert into users (username,status) values ("brisa",1)')
        try:
            res = Db('select').select('select * from users')
            return '-> {}'.format(res)
        except:
            return 'erro ao coletar informações'
    except:
        return 'erro ao inserir'