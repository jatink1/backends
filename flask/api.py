# # from flask import Flask, escape, request,jsonify
# # from flask_cors import CORS, cross_origin
# #
# # app = Flask(__name__)
# # cors = CORS(app)
# #
# # app.config['CORS_HEADERS'] = 'Content-Type'
# #
# # @app.route('/')
# # @cross_origin()
# # def hello():
# #     return jsonify({"about":"This works"})
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
# #
# # #logging.getLogger('flask_cors').level = logging.DEBUG
#
#
#
#
# from flask import Flask
# from flask_restful import Resource, Api
# from flask_cors import CORS
#
# # app = Flask(__name__)
#
# #
# # app = Flask(__name__)
# # cors = CORS(app)
# app = Flask(__name__)
# api = Api(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#     def options (self):
#             return { 'Access-Control-Allow-Origin': '*', \
#                  'Access-Control-Allow-Methods' : 'PUT,GET' }
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask,jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({"error": "Invalid email"})

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
