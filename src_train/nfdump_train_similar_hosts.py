import math
import argparse


def distance(original_features, cmp_features, type, n = 2):
    """
    Common function for compute distances between two vectors
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :param type: Type of distance metrics eg. minkowski distance, euclidean dist. etc.
    :param n: Parameter for minkowski dist.
    :return: Distance of two vectors using selected metrics
    """
    if type == "minkowski":
         return minkowski_distance(original_features, cmp_features, n)
    elif type == "euclidean":
        return minkowski_distance(original_features, cmp_features, 2)
    elif type == "sqeuclidean":
        return sq_euclidean_distance(original_features, cmp_features)
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
        dist += ((int(original_features[i]) - int(cmp_features[i])) ** m)
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


def split_record(record):
    """
    Removes whitespaces, removes newlines and splits record
    :param record: Record consists of sourceIP, no. of flows and no. of packets separated by ','
    :return: sourceIP, flows and packets separately
    """
    "".join(record.split())
    record.rstrip()
    return record.split(",")


def count_distances_for_ip(sourceIP, flows, packets, data, a = False):
    """
    Counts distance of one IP from all others
    :param sourceIP: IP of source
    :param flows: No. of flows of source
    :param packets: No. of packets of source
    :param data: Data of all others IP
    :param a: If compute whole line or just "upper triangle", using if compute distances of all IP to all IP or 1 to all
    :return: Distances of selected source IP to all others
    """
    distances = [sourceIP]
    saw = False
    for line in data.splitlines():
        cmp_sourceIP, cmp_flows, cmp_packets = split_record(line)
        if sourceIP == cmp_sourceIP and not saw:
            saw = True
            distances.append(0)
        elif not saw and not a:
            distances.append(-1)
        else:
            distances.append(distance([flows, packets], [cmp_flows, cmp_packets],"minkowski", n = 2))
    return distances


def get_similar_host(sourceIP, data, k):
    """
    Get the most similar host to selected source IP
    :param sourceIP: Source IP
    :param data: Data of all others IP
    :param k: For future use (knn)
    :return: Most similar host from selected IP and its distance
    """
    distances = count_distances(data)
    position = 0
    for i in range(1, len(distances[0])):
        if distances[i][0] == sourceIP:
            position = i
    minimum = math.inf
    ip = None
    for i in range(1, distances[position]):
        if distances[position][i] < minimum and i != position:
            minimum = distances[position][i]
            ip = distances[0][i]

    return ip, minimum


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
    Counts distances to of all IP from all IP
    :param data: Data of IP adresses, flows and packets
    :return: Matrix of distances between all IP
    """
    i = 0
    distances = [[None]]
    for line in data.splitlines():
        sourceIP, _ , _ = split_record(line)
        distances[0].append(sourceIP)
    for line in data.splitlines():
        sourceIP, flows, packets = split_record(line)
        print("Counting distances for ip " + sourceIP)
        i += 1
        distances.append(count_distances_for_ip(sourceIP, flows, packets, data, a = False))
        print("Done, " + str(i) + " of 150885 done")
        print(i/150885)

    for i in range(1,len(distances[0])):
        for j in range(i, len(distances[0])):
            distances[j][i] = distances[i][j]
    return distances

"""
For output to csv file
"""

csv_output = False


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", default=None,  help="Provide an source IP adress")
    parser.add_argument("-t", default=1000, help="Maximal distance for include the result IP")
    parser.add_argument("-n", default=10, help="First n closest adresses")
    namespace = parser.parse_args()

    if csv_output:
        out = open("similar_hosts.csv", "w")
        out.write("srcip;srcfl;srcpck;simip;simfl;simpck;score\n")

    data = load_data()
    for line in data.splitlines():
        sourceIP, flows, packets = split_record(line)
        similar_host, score = get_similar_host(sourceIP, data, k)
        if csv_output:
            out.write(str(sourceIP) + ";" + str(flows) + ";" + str(packets).rstrip() + ";" + str(similar_host[0]) + ";"
                      + str(similar_host[1]) + ";" + str(similar_host[2]).rstrip() + ";" + str(score) + "\n")

        else:
            print(sourceIP)
            print(similar_host)
            print(score)
            print()

    if csv_output:
        out.close()


if __name__ == "__main__":
    main()
