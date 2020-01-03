from flask import Flask
from flask_restful import Resource, Api

from src.similarity_search.similarity_search_main import lof_main, knn_main, range_main, distance_main, detail_main


class LOF(Resource):
    """
    This class represents api for LOF query
    """

    def get(self, host):
        return lof_main(host)


class KNN(Resource):
    """
    This class represents api for knn query.
    """

    def get(self, view, host, k, t):
        return knn_main(view, host, k, t)


class Range(Resource):
    """
    This class represents api for range query.
    """

    def get(self, distanceFunction, host, range):
        return "Not implemented yet"


class Detail(Resource):
    """
    Gets details about.md specific host
    """

    def get(self, host):
        return detail_main(host)


class Distance(Resource):
    """
    Counts distance between two hosts
    """

    def get(self, host1, host2):
        return distance_main(host1, host2)


def app_run():
    """
    Runs the app
    """

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(LOF, '/lof/<string:host>')
    api.add_resource(KNN, '/knn/<string:view>/<string:host>/<int:k>/<float:t>')
    api.add_resource(Range, '/range/<string:host>/<float:range>')
    api.add_resource(Detail, '/detail/<string:host>')
    api.add_resource(Distance, '/distance/<string:host1>/<string:host2>')
    app.run(debug=True)
