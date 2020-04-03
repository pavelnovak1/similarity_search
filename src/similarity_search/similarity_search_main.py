from data_tools import SQLCommands as sql_commands
from similarity_search import knn, range_search
from similarity_search.lof import lof as local_outlier_factor
import re

NUMBER_OF_FEATURES = 18

sql = sql_commands.SQLCommands()


def lof_main(host, ip_range=None, k=5):
    """
    Count Local outlier factor for specified host in given ip_range.
    """
    try:
        (sql.get_host_profile(host))[0][1:]  # Loading host profile
    except IndexError:
        return "IP not found"
    return local_outlier_factor(host, ip_range, k)


def lof_range_main(ip_range):
    """
    Count Local outlier factor of all devices in given range of addresses;
    """
    result = {}
    for ip in sql.load_range_addresses(ip_range)[0]:
        if not ip in result.keys():
            result[ip] = lof_main(ip, ip_range)
    return result


def lof_interrange_main(source_range, target_range):
    """
    Count Local outlier factor of all devices in source_range like they were part of target range.
    """
    counted = []
    for ip in sql.load_database_range(source_range):
        if not ip[0] in counted:
            counted.append(ip[0])
            sql.set_lof_interrange(ip[0], lof_main(ip[0], target_range))


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


def range_main(host, t):
    return range_search.range(host, t)


def detail_main(host):
    return sql.host_get_raw_info(host)
