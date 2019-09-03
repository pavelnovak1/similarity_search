import math

def minkowski_distance(original_features, cmp_features, m):
    dist = 0
    for i in range(len(original_features)):
        dist += ((int(original_features[i]) - int(cmp_features[i])) ** m)
    return math.pow(dist, 1/m)

def sq_euclidean_distance(original_features, cmp_features):
    """
    Compute squared euclidean distance between two records
    :param original_features: features like no. of flows or no. of packets of original record
    :param cmp_features: features like no. of flows or no. of packets of compared record
    :return: squared Euclidean distance between original and compared records
    """
    dist = 0
    for i in range(len(original_features)):
        dist += ((int(original_features[i]) - int(cmp_features[i])) ** 2)
    return dist

def euclidean_distance(original_features, cmp_features):
    """
    Compute euclidean distance between two records
    :param original_features: features like no. of flows or no. of packets of original record
    :param cmp_features: features like no. of flows or no. of packets of compared record
    :return: Euclidean distance between original and compared records
    """
    dist = 0
    for i in range(len(original_features)):
        dist += ((int(original_features[i]) - int(cmp_features[i])) ** 2)
    return math.sqrt(dist)


def split_record(record):
    """
    Remove whitespaces remove newline and splits record
    :param record: record consist of sourceIP, no. of flows and no. of packets separated by ','
    :return: sourceIP, flows and packets separately
    """
    "".join(record.split())
    record.rstrip()
    return record.split(",")


def get_similar_host(sourceIP, flows, packets):
    """
    Return the most similar record to given record (sourceIP, flows, packets)
    :param sourceIP: IP of the original record
    :param flows: no. of flows of the original record
    :param packets: no. of packets of the original record
    :return: The most similar record acording the euclidean distance
    """
    similar_score = math.inf
    similar_host = None
    s = open("nfdump_anonn_srcadrr_flows_pakets", "r")
    for r in s.readlines():
        cmp_sourceIP, cmp_flows, cmp_packets = split_record(r)
        if sourceIP == cmp_sourceIP:
            continue
        dist = minkowski_distance([flows, packets,int(packets)/int(flows)], [cmp_flows, cmp_packets, int(cmp_packets)/int(cmp_flows)],10)
        if (dist < similar_score):
            similar_score = dist
            similar_host = [cmp_sourceIP, cmp_flows, cmp_packets]
    s.close()
    return similar_score, similar_host





csv_output = False

nfdump_stats = open("nfdump_anonn_srcadrr_flows_pakets", "r")
if(csv_output):
    out = open("similar_hosts.csv", "w")
    out.write("srcip;srcfl;srcpck;simip;simfl;simpck;score\n")
    out.close()

for record in nfdump_stats.readlines():

    sourceIP, flows, packets = split_record(record)
    score, similar_host = get_similar_host(sourceIP, int(flows), int(packets))
    if(csv_output):
        out = open("similar_hosts.csv", "a")
        out.write(str(sourceIP) + ";" + str(flows) + ";" + str(packets).rstrip() + ";" + str(similar_host[0]) + ";"
                + str(similar_host[1]) + ";" + str(similar_host[2]).rstrip() + ";" + str(score) + "\n")
        out.close()
    else:
        print("Original IP: " + str(sourceIP) + "| Original flows: " + str(flows) + "| Original packets: " + str(packets))
        print("Similar IP: " + str(similar_host[0]) + "| Similar flows: " + str(similar_host[1]) + "| Similar packets: " + str(similar_host[2]))
        print("Distance: " + str(score))
        print()
        print("###################################")
        print()

nfdump_stats.close()
