from data_tools import dataCollector as collector
from similarity_search import knn, range_search
from similarity_search.distance_functions.distance_functions import minkowski_distance
from similarity_search.lof import lof as local_outlier_factor
import json

NUMBER_OF_FEATURES = 18

dc = collector.dataCollector()


def lof_main(host):
    try:
        (dc.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    return local_outlier_factor(host, 5)

def knn_recount_main(view, host, k, t):
    try:
        (dc.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    if view not in ["overall", "traffic", "application"]:
        view = "overall"
    all_profiles = make_all_profiles(exc=host)
    host_profile = make_host_profile(host)
    nearest_neighbours = knn.k_nn(view, host_profile, all_profiles)  # All addresses sorted by distance (host, distance)
    result = {}
    last = 0
    for (h, d) in nearest_neighbours:  # for host, distance ..
        if len(result.keys()) < k and d <= t:  # if not k nearest neighbours yet and closer than threshold, append
            result[h] = d
            last = d
        else:
            if d == last:
                result[h] = d
                continue
            return result
    return result

def knn_main(host, k, t):
    nearest_neighbours = dc.get_knn(host)[0][0]
    result = {}
    last = 0
    for h, d in nearest_neighbours.items():  # for host, distance ..
        if len(result.keys()) < k and d <= t:  # if not k nearest neighbours yet and closer than threshold, append
            result[h] = d
            last = d
        else:
            if d == last:
                result[h] = d
                continue
            return result
    return result


def range_main(host, t):
    return range_search.range(host, t)

def detail_main(host):
    return dc.get_info_about_address(host)


def distance_main(host1, host2):
    profile1_in = dc.get_data_about_host(host1, direction="in")
    profile1_out = dc.get_data_about_host(host1, direction="out")
    profile2_in = dc.get_data_about_host(host2, direction="in")
    profile2_out = dc.get_data_about_host(host2, direction="out")

    p1_in = missing_statistics_handling(profile1_in)
    p1_out = missing_statistics_handling(profile1_out)
    p2_in = missing_statistics_handling(profile2_in)
    p2_out = missing_statistics_handling(profile2_out)
    return minkowski_distance(p1_in + p1_out, p2_in + p2_out, 2)


def missing_statistics_handling(profile):
    if len(profile) != 1:
        profile = [(0,) * NUMBER_OF_FEATURES]
    return profile[0]


def make_stats(s):
    result = {}
    for profile in s:
        result[profile[0]] = profile[1:]
    return result

def make_host_profile(host=None):
    general = dc.get_general_statistics(host=host)
    advanced = dc.get_advanced_statistics(host=host)
    network = dc.get_network_layer_statistics(host=host)
    statistics = dc.get_statistic_features_statistics(host=host)
    application = dc.get_application_layer_statistics(host=host)
    return [general, advanced, network, statistics, application]

def make_all_profiles(exc=None):
    general = dc.get_general_statistics(exc=exc)
    advanced = dc.get_advanced_statistics(exc=exc)
    network = dc.get_network_layer_statistics(exc=exc)
    statistics = dc.get_statistic_features_statistics(exc=exc)
    application = dc.get_application_layer_statistics(exc=exc)
    return [general, advanced, network, statistics, application]
