# Host Behavior Similarity Search Tool

Use:

1. Run src.main
2. Using the GET function:
    - for ***knn query***: /knn/<string: host>/<int: k>/<float: t> 
    eg. /knn/239.36.249.160/5500/0.0003
If the address is not found, "IP not found" is displayed, otherwise the list of nearest addresses and their distance is displayed.

    - To display the ***address detail***, use / detail / <string: host> eg detail / 239.36.255.4
The address data is displayed if not found, IP not found is displayed.

    - for ***LOF*** query: / lof / <string: host> eg /lof/239.36.255.4
it is calculated and returns the LOF value for the address.

> 1 outlier

= 1 same as others

<1 inlier