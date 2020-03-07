from flask import Flask,jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({"Hello": "World"})

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
