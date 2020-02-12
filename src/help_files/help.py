def get_help():
    return "This is help for using this utility"

def get_help_lof():
    return "This is help for using lof similarity search"

def get_help_knn():
    return "Knn is used to find the nearest machines based on their behavior." \
           "The query is in the form / knn / <string: view> / <string: guest> / <int: k> / <float: t>" \
           "where view are predefined weights. For more information about the view, see / help / views. " \
           "Host is the address I want to search for. K is a parameter that specifies how many nearest machines are searched." \
           "In the case of the same distance for the last machines, all are included in the result so that more than K machines can be the result. " \
           "T is a parameter specifying the maximum distance that is still included in the result. For too small t can result in less than K machines." \
           "Example:" \
           "/knn/overall/239.36.145.16/5/0.03" \
           "239.36.4.122	0.000007756573298058335" \
           "239.36.143.236	0.000007983137257309268" \
           "239.36.223.254	0.00000918831256457821" \
           "239.36.121.110	0.000009315313048587839" \
           "239.36.117.69	0.0000100911401109172" \

def get_help_range():
    return "This is help for using range search"

def get_help_view():
    return "This is help for views"