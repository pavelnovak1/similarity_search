def count_view(view, distances):
    """
    Count final distance based on the specified view.
    :param view: One of the following options: overall, traffic, application
    :param distances: Vector of distances between categories.
    :return: Final distance based on the specified view.
    """
    overall_view = (20, 20, 20, 20, 20)
    traffic_volume_view = (20, 10, 50, 10, 10)
    application_view = (5, 5, 10, 30, 50)

    if view == "overall":
        return dot(overall_view, distances) / 100
    if view == "traffic":
        return dot(traffic_volume_view, distances) / 100
    if view == "application":
        return dot(application_view, distances) / 100


def dot(x, y):
    """
    Count dot product of two vectors.
    :param x: vector 1.
    :param y: vector 2.
    :return: Dot product of two vectors.
    """
    return sum(x_i * y_i for x_i, y_i in zip(x, y))
