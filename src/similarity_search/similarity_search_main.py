from data_tools import SQLCommands as sql_commands
from similarity_search import knn, range_search
from similarity_search.distance_functions.distance_functions import minkowski_distance
from similarity_search.lof import lof as local_outlier_factor
import re

NUMBER_OF_FEATURES = 18

sql = sql_commands.SQLCommands()


def lof_main(host, ip_range=None, k=5):
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    return local_outlier_factor(host, ip_range, k)

def lof_range_main(ip_range):
    counted = []
    for ip in sql.load_database_range(ip_range):
        if not ip[0] in counted:
            counted.append(ip[0])
            sql.set_lof_servers(ip[0] , lof_main(ip[0], ip_range))
def lof_interrange_main(source_range, target_range):
    counted = []
    for ip in sql.load_database_range(source_range):
        if not ip[0] in counted:
            counted.append(ip[0])
            sql.set_lof_interrange(ip[0], lof_main(ip[0], target_range))

def knn_main(view, host, ip_range=None, k=5, t=0.05):
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    if ip_range is None:
        ip_range = re.search("[0-9]+[.][0-9]+[.][0-9]+", host).group() 
    return knn.k_nn(view, host, ip_range, k, t)

"""
def knn_main(host, k, t):
    nearest_neighbours = sql.get_knn(host)[0][0]
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
    
def knn_recount_main(view, host, k, t):
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
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
"""

def range_main(host, t):
    return range_search.range(host, t)


def detail_main(host):
    return sql.host_get_raw_info(host)


def distance_main(host1, host2):
    profile1_in = sql.host_get_raw_info_directions(host1, direction="in")
    profile1_out = sql.host_get_raw_info_directions(host1, direction="out")
    profile2_in = sql.host_get_raw_info_directions(host2, direction="in")
    profile2_out = sql.host_get_raw_info_directions(host2, direction="out")

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
    general = sql.general(host=host)
    advanced = sql.advanced(host=host)
    network = sql.network(host=host)
    statistics = sql.statistics(host=host)
    application = sql.application(host=host)
    return [general, advanced, network, statistics, application]


def make_all_profiles(exc=None):
    general = sql.general(exc=exc)
    advanced = sql.advanced(exc=exc)
    network = sql.network(exc=exc)
    statistics = sql.statistics(exc=exc)
    application = sql.application(exc=exc)
    return [general, advanced, network, statistics, application]
