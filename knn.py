from src.distance_functions import minkowski_distance


def k_nn(instance, instance_addr, instances):
    # TODO: implement caching
    """Computes the k-distance of instance as defined in paper. It also gatheres the set of k-distance neighbours.
    Returns: (k-distance, k-distance neighbours)
    Signature: (int, (attr1, attr2, ...), ((attr_1_1, ...),(attr_2_1, ...), ...)) -> (float, ((attr_j_1, ...),(attr_k_1, ...), ...))"""
    distances = {}
    for ip in instances:
        if ip == instance_addr:
            continue
        distance_value = minkowski_distance(instance, instances[ip], 2)
        if distance_value in distances:
            distances[distance_value].append(ip)
        else:
            distances[distance_value] = [ip]
    distances = sorted(distances.items())
    return distances