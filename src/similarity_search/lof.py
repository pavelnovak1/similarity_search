from cmath import inf


def k_distance(host, ip_range, k):
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main("overall", host, ip_range, k, inf)
    return [list(knn.values()).pop(k - 1), knn]


def reachability_distance(host1, host2, ip_range, k):
    from similarity_search.similarity_search_main import distance_main
    return max(k_distance(host2, ip_range, k)[0], distance_main(host1, host2))

def local_reachability_density(host, ip_range, k):
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main("overall", host, ip_range, k, inf)
    tmp = 0
    for neighbour in knn:
        tmp += reachability_distance(host, neighbour, ip_range, k)
    return len(knn)/tmp

def lof(host, ip_range, k):
    lrd = local_reachability_density(host, ip_range, k)
    tmp = 0
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main("overall", host, ip_range, k, inf)
    for neighbour in knn:
        tmp += local_reachability_density(neighbour, ip_range, k)/lrd
    return tmp/len(knn)
