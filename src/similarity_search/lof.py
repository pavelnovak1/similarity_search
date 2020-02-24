from cmath import inf


def k_distance(host, k):
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main(host, k, inf)
    return [list(knn.values()).pop(k - 1), knn]


def reachability_distance(host1, host2, k):
    from similarity_search.similarity_search_main import distance_main
    return max(k_distance(host2, k)[0], distance_main(host1, host2))

def local_reachability_density(host, k):
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main(host, k, inf)
    tmp = 0
    for neighbour in knn:
        tmp += reachability_distance(host, neighbour, k)
    return len(knn)/tmp

def lof(host, k):
    lrd = local_reachability_density(host, k)
    tmp = 0
    from similarity_search.similarity_search_main import knn_main
    knn = knn_main(host, k, inf)
    for neighbour in knn:
        tmp += local_reachability_density(neighbour, k)/lrd
    return tmp/len(knn)
