from src import dataCollector as collector, knn
from src.lof import LOF, k_nn
from src.distance_functions import minkowski_distance
NUMBER_OF_FEATURES = 18

dc = collector.dataCollector()


def lof_main(host):
    profile = dc.get_host_profile(host)
    stats = dc.get_all_profiles()
    lof = LOF(stats, normalize=False)
    return lof.local_outlier_factor(5, profile[0])


def knn_main(host, k, t):
    profile = dc.get_host_profile(host)[0][1:]
    stats = make_stats(dc.get_all_profiles())
    nearest_neighbours = knn.k_nn(profile, host, stats)
    result = []
    print(len(stats))
    print(len(nearest_neighbours))
    for (d, h) in nearest_neighbours:
        for addr in h:
            if len(result) < k or d > t:
                result.append(addr)
            else:
                return result
    return result





def range_main(f, host, t):
    pass


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
    return minkowski_distance(p1_in, p2_in, p1_out, p2_out, 2)


def missing_statistics_handling(profile):
    if len(profile) != 1:
        profile = [(0,) * NUMBER_OF_FEATURES]
    return profile[0]


def make_stats(s):
    result = {}
    for profile in s:
        result[profile[0]] = profile[1:]
    return result
