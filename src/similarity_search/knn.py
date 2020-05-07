from similarity_search.distance_functions.distance_functions import minkowski_distance
from similarity_search.distance_functions.views import count_view
from data_tools import SQLCommands as sqlCommands

sql = sqlCommands.SQLCommands()


def k_nn(view, host, ip_range, k, t):
    """
    Count k nearest neighbors to the host
    """
    distances = {}
    host_profile = sql.profiles_categories(ip_range, host)[0]
    profiles = sql.profiles_categories(ip_range)

    for device in profiles:
        if device[0] == host:
            continue
        else:
            distance_vector = [0, 0, 0, 0, 0]
            for i in range(5):
                distance_vector[i] = minkowski_distance(device[i + 1], host_profile[i + 1], 2)
            distances[device[0]] = count_view(view, tuple(distance_vector))

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
