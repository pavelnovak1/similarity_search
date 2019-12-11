import math

def minkowski_distance(instance1, instance2, k):

    # check if instances are of same length
    if len(instance1) != len(instance2):
        raise AttributeError("Instances have different number of arguments.")
    # init differences vector
    differences = [0] * len(instance1)
    # compute difference for each attribute and store it to differences vector
    for i, (attr1, attr2) in enumerate(zip(instance1, instance2)):
        differences[i] = attr1 - attr2
    # compute RMSE (root mean squared error)
    rmse = (sum(map(lambda x: x ** k, differences)) / len(differences)) ** (1/k)
    return rmse

#def minkowski_distance(host1_in, host1_out, host2_in, host2_out, m):
#    dist = 0
#    for i in range(len(host1_in) - 1):
#        dist += abs(((int(host1_in[i]) - int(host2_in[i])) ** m))
#    for i in range(len(host1_out) - 1):
#        dist += abs(((int(host1_out[i]) - int(host2_out[i])) ** m))
#    return math.pow(dist, 1 / m)


def sq_euclidean_distance(original_features, cmp_features):
    """
    Compute squared euclidean distance between two records
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :return: Squared Euclidean distance between two vectors
    """
    dist = 0
    for i in range(len(original_features) - 1):
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
        a += int(original_features[i]) * int(cmp_features[i])
    for j in range(len(original_features)):
        b += int(original_features[j]) ** 2
    for k in range(len(cmp_features)):
        c += int(cmp_features[k]) ** 2
    return a / (math.sqrt(b) * math.sqrt(c))
