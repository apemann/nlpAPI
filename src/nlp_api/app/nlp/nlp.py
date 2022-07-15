from cProfile import label
from flask import request, jsonify
from flask_restful import Resource, reqparse
from itertools import groupby
import spacy

class NounsVerbs(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
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

        ents = []

        for entity in doc.ents:
            ent = {}
            ent['start_char'] = entity.start_char
            ent['end_char'] = entity.end_char
            ent['label_code'] = entity.label
            ent['label'] = entity.label_
            ent['text'] = entity.text

            ents.append(ent)

        return jsonify(ents)


class CondensedNer(Resource):
    nlp = spacy.load("en_core_web_sm")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('body')
        args = parser.parse_args()
        
        doc = self.nlp(args['body'])

        entities = {key: list(set(map(lambda x: str(x), g))) for key, g in groupby(sorted(doc.ents, key=lambda x: x.label_), lambda x: x.label_)}

        return jsonify(entities)