from collections import defaultdict
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def default_desk_status():
    status = {
        "status": "free",
        "name": "",
        "until": ""
        }
    return status


desk_status = defaultdict(default_desk_status)


class DeskStatus(Resource):
    def get(self, desk_id):
        return {desk_id: desk_status[desk_id]}


api.add_resource(DeskStatus, '/<string:desk_id>')

if __name__ == '__main__':
    app.run(debug=True)
