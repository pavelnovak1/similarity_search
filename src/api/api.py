from flask import Flask
from flask_restful import Resource, Api

from help_files.help import get_help, get_help_knn, get_help_lof, get_help_range, get_help_view
from similarity_search.similarity_search_main import lof_main, knn_main, range_main, distance_main, detail_main, knn_recount_main


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
        return knn_recount_main(view, host, k, t)


class Range(Resource):
    """
    This class represents api for range query.
    """

    def get(self, host, range):
        return range_main(host, range)


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


class UtilityHelp(Resource):
    """
    Help
    """

    def get(self, help_class):
        if not help_class in ["knn", "lof", "range"]:
            return get_help()
        elif help_class == "knn":
            return get_help_knn()
        elif help_class == "lof":
            return get_help_lof()
        elif help_class == "range":
            return get_help_range()
        elif help_class == "view":
            return get_help_view()


class Help(Resource):
    def get(self):
        return get_help()


class Hello(Resource):
    def get(self):
        return "Hello"


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
    api.add_resource(UtilityHelp, '/help/<string:help_class>')
    api.add_resource(Hello, '/')
    api.add_resource(Help, '/help')
    app.run(debug=True)
