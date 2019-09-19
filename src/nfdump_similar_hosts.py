import math
import argparse


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
         return minkowski_distance(original_features, cmp_features, n)
    elif t == "euclidean":
        return minkowski_distance(original_features, cmp_features, 2)
    elif t == "sqeuclidean":
        return sq_euclidean_distance(original_features, cmp_features)
    elif t == "cosine":
        return cosine_similarity(original_features, cmp_features)
    else:
        return -1


def minkowski_distance(original_features, cmp_features, m):
    """
    Function to compute a Minkowski distance between two vectors
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :param m: Parameter for compute Minkowski distance
    :return: Minkowski distance between two vectors
    """
    dist = 0
    for i in range(len(original_features)):
        dist += abs(((int(original_features[i]) - int(cmp_features[i])) ** m))
    return math.pow(dist, 1/m)


def sq_euclidean_distance(original_features, cmp_features):
    """
    Compute squared euclidean distance between two records
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :return: Squared Euclidean distance between two vectors
    """
    dist = 0
    for i in range(len(original_features)):
        dist += ((int(original_features[i]) - int(cmp_features[i])) ** 2)
    return dist


def cosine_similarity(original_features, cmp_features):
    """
        Compute cosine distance between two records
        :param original_features: Features like no. of flows or no. of packets of original record
        :param cmp_features: Features like no. of flows or no. of packets of compared record
        :return: Cosine distance between two vectors
        """
    a = 0
    b = 0
    c = 0
    for i in range(len(original_features)):
        a += int(original_features[i])*int(cmp_features[i])
    for j in range(len(original_features)):
        b += int(original_features[j])**2
    for k in range(len(cmp_features)):
        c += int(cmp_features[k])**2
    return a/(math.sqrt(b)*math.sqrt(c))


def args_control(a, t, n):
    """
    Controls if input parameters are correct
    :param a: Address
    :param t: Threshold
    :param n: First n records
    :return: True if all three arguments are correct, False otherwise
    """
    if a is None or t < 0 or n < 0:
        return False
    return True


def split_record(record):
    """
    Removes whitespaces, removes newlines and splits record
    :param record: Record consists of sourceIP, no. of flows and no. of packets separated by ','
    :return: sourceIP, flows and packets separately
    """
    "".join(record.split())
    record.strip()
    return record.split(",")


def count_distances_for_ip(sourceIP_record, data):
    """
    Counts distances from given IP address to all others. Distance from given IP to given IP is set to -1.
    :param sourceIP_record: SrcIP record in format: (srcIP, flows, packets)
    :param data: All records
    :return: Dictionary of all distances in format {IP:dist}
    """
    result = {}
    for line in data.splitlines():
        cmpIP, cmp_flows, cmp_packets = split_record(line)
        if cmpIP == sourceIP_record[0]:
            result[cmpIP] = -1
            continue
        else:
            result[cmpIP] = distance([sourceIP_record[1], sourceIP_record[2]], [cmp_flows, cmp_packets], "minkowski", 2)
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
    for address, flows, packets in similar_addresses:
        distances = count_distances_for_ip((address, flows, packets), data)
        d = distances.copy()
        for IP, dist in d.items():
            if dist > maxdist:
                del distances[IP]
        distances = sorted(distances.items(), key=lambda kv: kv[1], reverse=False)
        distances.pop(0)
        if len(distances) <= k+1:
            similar_hosts[address] = distances
        else:
            tmp = []
            for i in range(k):
                tmp.append(distances[i])
            similar_hosts[address] = tmp
    return similar_hosts


def load_data():
    """
    Loads data from file to variable
    :return: Data from file in variable
    """
    nfdump_stats = open("nfdump_anonn_srcadrr_flows_pakets", "r")
    data = ""
    for record in nfdump_stats.readlines():
        data += record
    nfdump_stats.close()
    return data


def count_distances(data):
    """
    Counts distances of all IP from all IP
    :param data: Data of IP addresses, flows and packets
    :return: Matrix of distances between all IP
    """
    pass


def get_similar_addresses(sourceIP, data):
    """
    Gets all addresses, its number of packets and flows for given network/sourceIP.
    :param sourceIP: Network address(eg. 147.250.240) or work station address(eg.147.250.240.39)
    :param data: All records
    :return: List of elements in form (IP, no. of flows of that IP, no. of packets of that IP) where IP is
    in given network.
    """
    similar_addresses = []
    for line in data.splitlines():
        cmpIP, cmp_flows, cmp_packets = split_record(line)
        cmpIP = cmpIP.strip()
        for i in range(len(sourceIP)):
            if sourceIP[i] == cmpIP[i]:
                if (i+1) == len(sourceIP):
                    similar_addresses.append((cmpIP, cmp_flows, cmp_packets))#
                else:
                    continue

            else:
                break

    return similar_addresses

def find_packets_flows(IP):
    d = load_data()
    for line in d.splitlines():
        srcIP, packets, flows = split_record(line)
        if str(IP).strip() == str(srcIP).strip():
            print("IP: " + IP + " packets " + packets + " flows " + flows)
            return

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", default=None,  help="Provide an source IP adress")
    parser.add_argument("-t", default=1000, help="Maximal distance for include the result IP")
    parser.add_argument("-n", default=10, help="First n closest adresses")
    namespace = parser.parse_args()

    if not args_control(namespace.a, int(namespace.t), int(namespace.n)):
        print("Invalid options")
        return -1

    data = load_data()
    print("Searching for similar hosts for network/host: " + namespace.a)
    print("Threshold: " + str(namespace.t))
    print("Number of nearest hosts: ", str(namespace.n))
    print("_________________________________________________________")

    result = get_similar_hosts(namespace.a, int(namespace.n), int(namespace.t), data)
    if len(result) == 0:
        print("Network " + namespace.a + " was not found or no address satisfies threshold ", str(namespace.t))
        return 0
    print("Number of addresses found on network ", namespace.a,": ", len(result))
    for IP, hosts in result.items():
        print("IP: " + IP)
        for simIP, d in hosts:
            print("Similar host: " + simIP + " in distance: " + str(d))

        if len(hosts) == 0:
            print("Threshold " + str(namespace.t) + " is too big. No addresses satisfied")
        print()
        print("_________________________________________________________")


if __name__ == "__main__":
    main()
