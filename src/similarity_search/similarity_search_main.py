from data_tools import sql_commands as sql_c
from similarity_search import knn, range_search
from similarity_search.lof import lof as local_outlier_factor
from similarity_search.distance_functions.distance_functions import minkowski_distance
from similarity_search.distance_functions.views import count_view
import math
import re
import numpy

sql = sql_c.sql_commands()

def update_borders(ip_range):
    result = set()
    for ip in sql.get_ip_range(ip_range):
        result.update(knn.k_nn("overall", ip[0], ip_range, math.inf, math.inf).values())
    result = list(sorted(result))
    sql.update_quantiles(ip_range, numpy.quantile(result, 0.25), numpy.quantile(result, 0.5), numpy.quantile(result, 0.75))

def lof_main(host, ip_range=None, k=5):
    """
    Count Local outlier factor for specified host in given ip_range.
    """
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    lof = local_outlier_factor(host, ip_range, k)
    return lof


def lof_range_main(ip_range, k=5):
    """
    Count Local outlier factor of all devices in given range of addresses;
    """
    result = {}
    for ip in sql.get_ip_range(ip_range):
        if not ip[0] in result.keys():
            result[ip[0]] = lof_main(ip[0], ip_range, k)
            print( ip[0] )
            print( result[ip[0]] )
    return result

def scanner_main(ip_range):
    l = lof_range_main(ip_range, 3)
    if( len(l) == 0 ): return "IP range not found"
    result = {}
    mean = 0
    count = 0
    _sum = 0
    for ip in l:
        count += 1
        _sum += l[ip]
    mean = _sum/count
    for ip in l:
        if abs(l[ip] - mean) > 2*mean:
            graterLof = lof_main(ip, ip_range, 5)
            if abs(graterLof - mean) > mean:
                result[ip] = graterLof
    if len(result) > 0:
        return result
    return "No suspicious devices"


def lof_interrange_main(source_range, target_range):
    """
    Count Local outlier factor of all devices in source_range like they were part of target range.
    """
    result = {}
    for ip in sql.get_ip_range(source_range):
        if not ip[0] in result.keys():
            result[ip[0]] = lof_main(ip[0], target_range)
    return result


def knn_main(view, host, ip_range=None, k=5, t=0.05):
    """
    Count K nearest neighbours to host in specified range.
    """
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    if ip_range is None:
        ip_range = re.search("[0-9]+[.][0-9]+[.][0-9]+", host).group()
    return knn.k_nn(view, host, ip_range, k, t)

def knn_main_just_knn(view, host, ip_range=None, k=5, t=0.05):
    result = {}
    knn = knn_main(view, host, ip_range, k, t)
    q = sql.get_quantiles(ip_range)
    if len(q) != 0:
        q = q[0]
        for k, v in knn.items():
            if v < q[0]:
                result[k] = "Very close"
                continue
            if v < q[1]:
                result[k] = "Close"
                continue
            if v < q[2]:
                result[k] = "Far"
                continue
            result[k] = "Very Far"
        return result
    return knn


def range_main(host, t):
    return range_search.range(host, t)


def detail_main(host):
    return sql.host_get_raw_info(host)


def distance_main(host1, host2, view = "overall"):
    profile1 = sql.profiles_categories(None, host1)[0]
    profile2 = sql.profiles_categories(None, host2)[0]
    distance_vector = [0, 0, 0, 0, 0]
    for i in range(5):
        distance_vector[i] = minkowski_distance(profile1[i + 1], profile2[i + 1], 2)
    return count_view(view, tuple(distance_vector))
