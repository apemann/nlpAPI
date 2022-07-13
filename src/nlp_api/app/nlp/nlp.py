from flask import request, jsonify
from flask_restful import Resource, reqparse
import spacy

class NounsVerbs(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('body')
        args = parser.parse_args()
        print(args)
        doc = self.nlp(request.form['data'])
        return jsonify({"Noun phrases": [chunk.text for chunk in doc.noun_chunks],
                        "Verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]})


class Ner(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('body')
        args = parser.parse_args()
        doc = self.nlp(args['body'])

        return jsonify({"noun_phrases": [chunk.text for chunk in doc.noun_chunks],
                        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]})