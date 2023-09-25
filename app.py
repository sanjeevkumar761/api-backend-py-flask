

from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.OpenAIApiHandler import OpenAIApiHandler
from api.ConvApiHandler import ConvApiHandler
from api.CSVStreamer import CSVStreamer


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(OpenAIApiHandler, '/askquestion2')
api.add_resource(ConvApiHandler, '/askquestion')
api.add_resource(CSVStreamer, '/getcsv')
