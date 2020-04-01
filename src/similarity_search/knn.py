from similarity_search.distance_functions.distance_functions import minkowski_distance
from similarity_search.distance_functions.views import count_view
from data_tools import SQLCommands as sqlCommands

sql = sqlCommands.SQLCommands()

def k_nn(view, host, ip_range, k, t):
    """
    The function counts k nearest neighbors to the host
    :param view: view
    :param host: target host
    :param ip_range: range
    :return:
    """
    distances = {}
    host_profile = [sql.general(None, host), sql.advanced(None, host), sql.network(None, host)
                    , sql.statistics(None, host), sql.application(None, host)]
    for ip in sql.load_range_addresses(ip_range):
        if ip[0] == host:
            continue
        else:
            profile = [sql.general(None, ip[0]), sql.advanced(None, ip[0]), sql.network(None, ip[0])
                    , sql.statistics(None, ip[0]), sql.application(None, ip[0])]
            distance_vector = [0, 0, 0, 0, 0]
            for i in range(5):
                distance_vector[i] = minkowski_distance(profile[i], host_profile[i], 2)
            distances[ip[0]] = count_view(view, tuple(distance_vector))


    distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    result = {}
    last = 0
    for h, d in distances.items():  # for host, distance ..
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

def k_nn(view, host, ip_range, k, t):

    The function counts k nearest neighbors to the host
    :param view: view
    :param host: target host
    :param ip_range: range
    :return:

    distances = {}
    host_profile = sql.get_host_profile(host)[0][1:] #load host profile
    for ip in sql.load_database_range(ip_range):
        if ip[0] == host:
            continue
        else:
            distances[ip[0]] = minkowski_distance(host_profile, ip[1:], 2)
    distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    result = {}
    last = 0
    for h, d in distances.items():  # for host, distance ..
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

"""    
    distances = {}
    for device in range(len(all_profiles[0])):  # pro kazdou ntici v tabulce tj. pro kazdy pristroj
        distance_vector = [0, 0, 0, 0, 0]  # inicializuj vzdalenostni vektor
        ip_address = all_profiles[1][device][0]
        for feature_category in range(len(target_host_profile)):
            distance_vector[feature_category] = minkowski_distance(target_host_profile[feature_category][0][1:],
                                                                   all_profiles[feature_category][device][1:], 2)
        distance_value = count_view(view, tuple(distance_vector))

        distances[ip_address] = distance_value
    distances = sorted(distances.items(), key=lambda x: x[1])
    return distances

"""
