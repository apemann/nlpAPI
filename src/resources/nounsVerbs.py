from flask import request, jsonify
from flask_restful import Resource, reqparse
from main import parser
import spacy

class NounsVerbs(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
        args = parser.parse_args()
        print(args)
        doc = self.nlp(request.form['data'])
        return jsonify({"Noun phrases": [chunk.text for chunk in doc.noun_chunks],
                        "Verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]})

