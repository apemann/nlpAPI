from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.nlp.nlp import NounsVerbs, Ner

    
api = Api()

api.add_resource(Ner, '/ner', methods=['POST'])
api.add_resource(NounsVerbs, '/extractNounsVerbs', methods=['POST'])
  
  
def create_app():
    app = Flask(__name__)
    api.init_app(app)
    CORS(app)

    return app