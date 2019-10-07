import math

def minkowski_distance(original_features, cmp_features, m):
    """
    Function to compute a Minkowski distance between two vectors
    :param original_features: Features like no. of flows or no. of packets of original record
    :param cmp_features: Features like no. of flows or no. of packets of compared record
    :param m: Parameter for compute Minkowski distance
    :return: Minkowski distance between two vectors
    """
    dist = 0
    for i in range(len(original_features) - 1):
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
        a += int(original_features[i])*int(cmp_features[i])
    for j in range(len(original_features)):
        b += int(original_features[j])**2
    for k in range(len(cmp_features)):
        c += int(cmp_features[k])**2
    return a/(math.sqrt(b)*math.sqrt(c))

