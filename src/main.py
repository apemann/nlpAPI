from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from resources.square import Square
import spacy
# from resources.sentiment import Sentiment
  
app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('body')

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})
  
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  

class NounsVerbs(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
        args = parser.parse_args()
        doc = self.nlp(args['body'])

        return jsonify({"noun_phrases": [chunk.text for chunk in doc.noun_chunks],
                        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]})

  
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(NounsVerbs, '/extractNounsVerbs', methods=['POST'])
  
  
if __name__ == '__main__':
    app.run(debug = True)