from flask import Flask
from flask_restful import Resource, Api
from similarity_search.similarity_search_main import knn_main_just_knn, update_borders, scanner_main, \
    lof_interrange_main, lof_range_main, lof_main, knn_main, range_main, detail_main


class quantiles_api(Resource):
    """
    Api for recount and update quantiles.
    """

    def get(self, ip_range):
        """
        Recount and insert into 'quantiles' table new quantiles of distances between devices in a specified IP range.
        :param ip_range: Wanted IP range.
        :return: None.
        """
        return update_borders(ip_range)


class lof_api(Resource):
    """
    Api for LOF query.
    """

    def get(self, host, ip_range):
        """
        Return Local Outlier Factor of a specified device in a specified IP range.
        :param host: Wanted host.
        :param ip_range: Wanted IP range.
        :return: Value of a Local Outlier Factor.
        """
        return lof_main(host, ip_range)


class lof_range_api(Resource):
    """
    Api for LOF range query.
    """

    def get(self, ip_range):
        """
        Count a value of LOF for all devices in a given range.
        :param ip_range: Wanted IP range.
        :return: Value of a Local Outlier Factor for each device in a specified IP range.
        """
        return lof_range_main(ip_range)


class lof_inter_range_api(Resource):
    """
    Api for Lof Inter Range query.
    """

    def get(self, source_range, target_range):
        """
        LOF of all devices in source range like they were in a specified range.
        :param source_range: Source IP range.
        :param target_range: Target IP range.
        :return: Value of a Local Outlier Factor of each device in a source IP range like it was in a target IP range.
        """
        return lof_interrange_main(source_range, target_range)


class knn_api(Resource):
    """
    Api for KNN query.
    """

    def get(self, view, host, ip_range, k, t):
        """
        Return K nearest neighbours for a given host.
        :param view: View used to determine the distance between devices.
        :param host: Wanted host.
        :param ip_range: Wanted IP range.
        :param k: K parameter.
        :param t: Threshold. All devices further this distance will not be included into the result.
        :return:
        """
        return knn_main_just_knn(view, host, ip_range, k, t)


class scanner_api(Resource):
    """
    Api for scan function.
    """

    def get(self, ip_range):
        """
        Scan the specified IP range and select suspected devices.
        :param ip_range: Wanted IP range.
        :return: Potentially suspected devices.
        """
        return scanner_main(ip_range)


class range_api(Resource):
    """
    Api for a range query.
    """

    def get(self, host, t):
        """
        Return all devices closer than a specified threshold.
        :param host: Wanted host.
        :param t: Threshold.
        :return: All devices closer than the specified threshold.
        """
        return range_main(host, t)


class detail_api(Resource):
    """
    Api for a detail query.
    """

    def get(self, host):
        """
        Return detail of a specified host.
        :param host: Wanted host.
        :return: Communication profile of the specified host.
        """
        return detail_main(host)


class hello_api(Resource):
    """
    Hello page.
    """
    def get(self):
        """
        Hello page
        :return: Hello.
        """
        return "Hello"


def app_run():
    """
    Runs the api
    """
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(lof_api, '/lof/<string:host>/<string:ip_range>')
    api.add_resource(knn_api, '/knn/<string:host>/<string:ip_range>/<string:view>/<int:k>/<float:t>')
    api.add_resource(range_api, '/range/<string:host>/<float:range>')
    api.add_resource(detail_api, '/detail/<string:host>')
    api.add_resource(lof_inter_range_api, '/lof/interrange/<string:source_range>/<string:target_range>')
    api.add_resource(hello_api, '/')
    api.add_resource(lof_range_api, '/lof/range/<string:ip_range>')
    api.add_resource(scanner_api, '/scan/<string:ip_range>')
    api.add_resource(quantiles_api, '/quantiles/<string:ip_range>')
    app.run(debug=True)
