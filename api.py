from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import psycopg2
import os

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://w205_final:w205_final@w205-final.cz7z0nmeyqpf.us-east-1.rds.amazonaws.com:5432/w205_final"
e = create_engine(SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
api = Api(app)

class Drugs(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("SELECT DISTINCT(drug_name) FROM loader_brands LIMIT 1000;")
        result = {"drugs": [i[0] for i in query.cursor.fetchall()]}
        return result

api.add_resource(Drugs, "/drugs")

if __name__ == "__main__":
    app.run( host = '0.0.0.0' )
