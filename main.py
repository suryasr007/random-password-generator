from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_args
from password_generator import PasswordGenerator

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()

'''
self.minlen = 6
self.maxlen = 16
self.minuchars = 1
self.minlchars = 1
self.minnumbers = 1
self.minschars = 1
self.excludeuchars = ""
self.excludelchars = ""
self.excludenumbers = ""
self.excludeschars = ""
'''

pwg = PasswordGenerator()

password_generator_args = {
    'minlen': fields.Int(missing=6, validate=lambda val: val > 0),
    'maxlen': fields.Int(missing=16, validate=lambda val: val > 0),
    'minuchars': fields.Int(missing=1, validate=lambda val: val > 0),
    'minuchars': fields.Int(missing=1, validate=lambda val: val > 0),
    'minlchars': fields.Int(missing=1, validate=lambda val: val > 0),
    'excludeuchars': fields.Str(missing=''),
    'excludelchars': fields.Str(missing=''),
    'excludenumbers': fields.Str(missing=''),
    'excludeschars': fields.Str(missing='')
}

class PasswordGenerator(Resource):

    @use_args(password_generator_args)
    def get(self, args):
        pwg.__dict__.update(args)
        try:
            res = pwg.generate()
        except ValueError as e:
            abort(404, str(e))
        
        return jsonify({'password':res})




api.add_resource(PasswordGenerator, '/generate')

if __name__ == '__main__':
    app.run()