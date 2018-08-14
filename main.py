from flask import Flask
from flask_restful import Resource, Api, reqparse
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
    'minlen': fields.Int(validate=lambda val: val > 0)
}

class PasswordGenerator(Resource):
    def get(self):
        parser.add_argument('minlen', type=int)
        parser.add_argument('maxlen', type=int)
        parser.add_argument('minuchars', type=int)
        parser.add_argument('minlchars', type=int)
        parser.add_argument('excludeuchars', type=str)
        parser.add_argument('excludelchars', type=str)
        parser.add_argument('excludenumbers', type=str)
        parser.add_argument('excludeschars', type=str)

        args = parser.parse_args()
        # td = {}
        # for k,v in args.items():
        #     if v is not None:
        #         td[k] = v
        
        # val = pwg.generate()
        return args




api.add_resource(PasswordGenerator, '/generate')

if __name__ == '__main__':
    app.run(debug=True)