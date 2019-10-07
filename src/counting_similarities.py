import distance_func

"""
Trida slouzici pro spocitani podobnych zarizeni na zaklade spoctenych statistik.
"""


def distance(original_features, cmp_features, t, n = 2):
    """
    Common function for compute distances between two vectors
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :param t: Type of distance metrics eg. minkowski distance, euclidean dist. etc.
    :param n: Parameter for minkowski dist.
    :return: Distance of two vectors using selected metrics
    """
    if t == "minkowski":
         return distance_func.minkowski_distance(original_features, cmp_features, n)
    elif t == "euclidean":
        return distance_func.minkowski_distance(original_features, cmp_features, 2)
    elif t == "sqeuclidean":
        return distance_func.sq_euclidean_distance(original_features, cmp_features)
    elif t == "cosine":
        return distance_func.cosine_similarity(original_features, cmp_features)
    else:
        return -1

def count_distances_for_ip(sourceIP, data):
    """
    Counts distances from given IP address to all others. Distance from given IP to given IP is set to -1.
    :param sourceIP_record: SrcIP record in format: (srcIP, flows, packets)
    :param data: All records
    :return: Dictionary of all distances in format {IP:dist}
    """
    result = {}
    for cmpIP in data:
        if cmpIP == sourceIP:
            result[cmpIP] = -1
            continue
        else:
            result[cmpIP] = distance(data[sourceIP], data[cmpIP], "minkowski", 2)
    return result


def get_similar_hosts(sourceIP, k, maxdist, data):
    """
    Offers k nearest addresses and its distances from sourceIP if distance is not bigger than maxdist.
    :param sourceIP: IP of source
    :param k: Knn parameter
    :param maxdist: Maximum distance allowed
    :param data: All records
    :return: K-nearist neighbours to given sourceIP. If distance is bigger than maxdist param. it is not included
    to the result.
    """

    similar_addresses = get_similar_addresses(sourceIP, data)
    similar_hosts = {}
    if len(similar_addresses) == 0:
        return {}
    for ip in similar_addresses:
        distances = count_distances_for_ip(ip, data)
        d = distances.copy()
        for IP, dist in d.items():
            if dist > maxdist:
                del distances[IP]
        distances = sorted(distances.items(), key=lambda kv: kv[1], reverse=False)
        distances.pop(0)
        if len(distances) <= k+1:
            similar_hosts[ip] = distances
        else:
            tmp = []
            for i in range(k):
                tmp.append(distances[i])
            similar_hosts[ip] = tmp
    return similar_hosts


def get_similar_addresses(sourceIP, data):
    """
    Gets all addresses, its number of packets and flows for given network/sourceIP.
    :param sourceIP: Network address(eg. 147.250.240) or work station address(eg.147.250.240.39)
    :param data: All records
    :return: List of elements in form (IP, no. of flows of that IP, no. of packets of that IP) where IP is
    in given network.
    """
    similar_addresses = []
    for key in data:
        for i in range(len(sourceIP)):
            if sourceIP[i] == key[i]:
                if (i+1) == len(sourceIP):
                    similar_addresses.append(key)
                elif (i+1) == len(key):
                    break
                else:
                    continue

            else:
                break
    print("Done, similar addresses found, total " + str(len(similar_addresses)))
    return similar_addresses


def main(data, ip='', t=1000, knn=10):

    print("Searching for similar hosts for network/host: " + ip)
    print("Threshold: " + str(t))
    print("Number of nearest hosts: ", str(knn))
    print("_________________________________________________________")

    return get_similar_hosts(ip, knn, t, data)




