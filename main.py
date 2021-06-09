from flask import Flask, jsonify, abort, render_template, request
from flask_restful import Resource, Api, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_args
from password_generator import PasswordGenerator
import re

app = Flask(__name__)
api = Api(app, prefix="/api")

parser = reqparse.RequestParser()

'''
Defaults
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

shuffle_password_args = {
    'maxlen': fields.Int(required={'message': 'maximum length required', 'code': 400}),
    'password': fields.Str(required={'message': 'Password required', 'code': 400})
}

non_duplicate_args = {
    'maxlen': fields.Int(required={'message': 'maximum length required', 'code': 400})
}


class PasswordGenerator(Resource):

    @use_args(password_generator_args, location="query")
    def get(self, args):
        try:
            pwg.__dict__.update(args)
            res = pwg.generate()
        except Exception as e:
            abort(404, str(e))

        return jsonify({'password': res})


class ShufflePassword(Resource):

    @use_args(shuffle_password_args, location="query")
    def get(self, args):
        try:
            res = pwg.shuffle_password(password=args["password"], maxlen=args["maxlen"])
        except Exception as e:
            abort(404, str(e))

        return jsonify({'password': res})


class NonDuplicatePassword(Resource):

    @use_args(non_duplicate_args, location="query")
    def get(self, args):
        try:
            res = pwg.non_duplicate_password(maxlen=args["maxlen"])
        except Exception as e:
            abort(404, str(e))

        return jsonify({'password': res})


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


api.add_resource(PasswordGenerator, '/generate')
api.add_resource(ShufflePassword, '/shuffle')
api.add_resource(NonDuplicatePassword, '/nonduplicate')

if __name__ == '__main__':
    app.run()
