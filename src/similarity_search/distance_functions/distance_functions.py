import math


def minkowski_distance(instance1, instance2, k):
    """
    Computes minkowski distance of two vectors
    :param instance1: vector 1
    :param instance2: vector 2
    :param k: k parameter
    :return: minkowski distance of two vectors
    """
    if len(instance1) != len(instance2):
        raise AttributeError("Instances have different number of arguments.")
    differences = [0] * len(instance1)
    for i, (attr1, attr2) in enumerate(zip(instance1, instance2)):
        differences[i] = attr1 - attr2
    result = (sum(map(lambda x: x ** k, differences)) / len(differences)) ** (1 / k)
    return result


def sq_euclidean_distance(instance1, instance2):
    """
    Computes squared euclidean distance of two vectors
    :param instance1: vector 1
    :param instance2: vector 2
    :return: Squared Euclidean distance of two vectors
    """
    if len(instance1) != len(instance2):
        raise AttributeError("Instances have different number of arguments.")
    dist = 0
    for i in range(len(instance1) - 1):
        dist += ((int(instance1[i]) - int(instance2[i])) ** 2)
    return dist


def cosine_similarity(instance1, instance2):
    """
        Computes cosine distance of two vectors
        :param instance1: vector 1
        :param instance2: vector 2
        :return: Cosine distance of two vectors
        """
    if len(instance1) != len(instance2):
        raise AttributeError("Instances have different number of arguments.")
    a = 0
    b = 0
    c = 0
    for i in range(len(instance1)):
        a += int(instance1[i]) * int(instance2[i])
    for j in range(len(instance1)):
        b += int(instance1[j]) ** 2
    for k in range(len(instance2)):
        c += int(instance2[k]) ** 2
    return a / (math.sqrt(b) * math.sqrt(c))
