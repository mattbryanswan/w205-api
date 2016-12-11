from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import psycopg2
import os
import json

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://w205_final:w205_final@w205-final.cz7z0nmeyqpf.us-east-1.rds.amazonaws.com:5432/w205_final"
e = create_engine(SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
api = Api(app)

class Drugs(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("(select drug_name, brand_name as name, 'brand' as type from fda_brands union select drug_name, generic_name as name, 'generic' as type from fda_generics) order by name asc;")
        data = {}
        for i in query.cursor.fetchall():
            data[i[1]] = [{'drug': i[0]}, {'type': i[2]}]

        return data

api.add_resource(Drugs, "/drugs")

if __name__ == "__main__":
    app.run( host = '0.0.0.0' )
