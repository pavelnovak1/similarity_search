def count_view(view, distances):
    """
    Count final distance based on view
    :param view: one of following: overall, traffic, application
    :param distances: distances
    :return: average value of distances
    """
    overall_view = (20, 20, 20, 20, 20)
    traffic_volume_view = (20, 10, 50, 10, 10)
    application_view = (5, 5, 10, 30, 50)

    if view == "overall":
        return dot(overall_view, distances)/100
    if view == "traffic":
        return dot(traffic_volume_view, distances)/100
    if view == "application":
        return dot(application_view, distances)/100

def dot(x, y):
    """Dot product as sum of list comprehension doing element-wise multiplication"""
    return sum(x_i*y_i for x_i, y_i in zip(x, y))