from src.similarity_search.distance_functions.distance_functions import minkowski_distance
from src.similarity_search.distance_functions.views import count_view


def k_nn(view, target_host_profile, all_profiles):
    """
    Count knn of given tsrget host
    :param view:
    :param target_host_profile:
    :param all_profiles:
    :return:
    """
    distances = {}
    for device in range(len(all_profiles[0])):  # pro kazdou ntici v tabulce tj. pro kazdy pristroj
        distance_vector = [0, 0, 0, 0, 0]  # inicializuj vzdalenostni vektor
        ip_address = all_profiles[1][device][0]
        for feature_category in range(len(target_host_profile)):
            distance_vector[feature_category] = minkowski_distance(target_host_profile[feature_category][0][1:],
                                                                   all_profiles[feature_category][device][1:], 2)
        distance_value = count_view(view, tuple(distance_vector))

        distances[ip_address] = distance_value
    distances = sorted(distances.items(), key=lambda x: x[1])
    return distances
