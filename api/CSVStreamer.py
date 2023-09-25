import os

from flask_restful import Api, Resource, reqparse
from flask import Response
import json

class CSVStreamer(Resource):
  # def get(self, place):
  def post(self):
    print("got request in OpenAICSVStreamerApiHandler")
    parser = reqparse.RequestParser()
    parser.add_argument('question', type=str)

    args = parser.parse_args()

    print(args)

    def generate():
        fruits = [{"fruit1":"apple"}, {"fruit2":"apple2"}, {"fruit3":"apple3"}]

        releases = fruits


        # We have some releases. First, yield the opening json
        #yield '{"releases": ['

        # Iterate over the releases
        #for release in releases:
        #    yield json.dumps(release) + ', '
        #    prev_release = release

        # Now yield the last iteration without comma but with the closing brackets
        # yield ']}'

        yield "" + '[{"fruit1":"apple"}, {"fruit2":"apple2"}, {"fruit3":"apple3"}]'

    return Response(generate(), content_type='application/json')


  