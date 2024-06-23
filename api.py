from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

items = {
  '1': {'name': 'item1', 'price': 100},
  '2': {'name': 'item2', 'price': 200},
  '3': {'name': 'item3', 'price': 300},
}


class ItemList(Resource):
  def get(self):
    return items


api.add_resource(ItemList, '/')

if __name__ == '__main__':
  app.run(debug=True)
