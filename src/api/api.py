from flask import Flask
from flask_restful import Resource, Api
from similarity_search.similarity_search_main import knn_main_just_knn, update_borders, scanner_main, lof_interrange_main, lof_range_main, lof_main, knn_main, range_main, detail_main

class Borders(Resource):

    def get(self, ip_range):
        return update_borders(ip_range)

class LOF(Resource):
    """
    This class represents api for LOF query
    """

    def get(self, host, ip_range):
        return lof_main(host, ip_range)

class LOFRange(Resource):
    """LOF of all devices within a given range"""
    def get(self, ip_range):
        return lof_range_main(ip_range)

class LOFInterRange(Resource):
    """LOF of all devices in source range within a target range"""
    def get(self, source_range, target_range):
        return lof_interrange_main(source_range, target_range)

class KNN(Resource):
    """
    This class represents api for knn query.
    """

    def get(self, view, host, ip_range, k, t):
        return knn_main_just_knn(view, host, ip_range, k, t)

class Scanner(Resource):

    def get(self, ip_range):
        return scanner_main(ip_range)


class Range(Resource):
    """
    This class represents api for range query.
    """

    def get(self, host, ip_range):
        return range_main(host, ip_range)


class Detail(Resource):
    """
    Gets details about.md specific host
    """

    def get(self, host):
        return detail_main(host)


class Hello(Resource):
    def get(self):
        return "Hello"


def app_run():
    """
    Runs the app
    """

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(LOF, '/lof/<string:host>/<string:ip_range>')
    api.add_resource(KNN, '/knn/<string:host>/<string:ip_range>/<string:view>/<int:k>/<float:t>')
    api.add_resource(Range, '/range/<string:host>/<float:range>')
    api.add_resource(Detail, '/detail/<string:host>')
    api.add_resource(LOFInterRange, '/lof/interrange/<string:source_range>/<string:target_range>')
    api.add_resource(Hello, '/')
    api.add_resource(LOFRange, '/lof/range/<string:ip_range>')
    api.add_resource(Scanner, '/scan/<string:ip_range>')
    api.add_resource(Borders, '/borders/<string:ip_range>')
    app.run(debug=True)
