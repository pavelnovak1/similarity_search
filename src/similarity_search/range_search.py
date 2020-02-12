from cmath import inf


def range(host, t):
    from src.similarity_search.similarity_search_main import knn_main
    return knn_main("overall", host, inf, t)