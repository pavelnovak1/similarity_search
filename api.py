from flask import Flask
from flask_restful import Resource, Api

from src.main import lof_main, knn_main, range_main,  distance_main, detail_main

app = Flask(__name__)
api = Api(app)

"""
This class represents api for LOF query for specific host
"""


class LOF(Resource):

    def get(self, host):
        return lof_main(host)


"""
This class represents api for knn query.
"""


class KNN(Resource):

    def get(self, host, k, t):
        return knn_main(host, k, t)


"""
This class represents api for range query.
"""


class Range(Resource):

    def get(self, distanceFunction, host, range):
        return range_main(distanceFunction, host, range)


"""
This class represents api for getting details about specific host
"""


class Detail(Resource):
    def get(self, host):
        return detail_main(host)


"""
This class allow to getting distance between two hosts
"""


class Distance(Resource):

    def get(self, host1, host2):
        return distance_main(host1, host2)


api.add_resource(LOF, '/lof/<string:host>')
api.add_resource(KNN, '/knn/<string:host>/<int:k>/<int:t>')
api.add_resource(Range, '/range/<string:distnaceFunction>/<string:host>/<float:range>')
api.add_resource(Detail, '/detail/<string:host>')
api.add_resource(Distance, '/distance/<string:host1>/<string:host2>')

if __name__ == '__main__':
    app.run(debug=True)
