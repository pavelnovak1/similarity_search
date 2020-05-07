# Host Behavior Similarity Search Tool
This tool was developed as part of my bachelor thesis. Its goal is to search for similar and different devices.

##Schema
The folder **data** contains all the data that was used to test the tool. The folder itself contains two *.csv* files that contain raw communication profiles. The *host_profile_ratios_anon.csv* file then contains the ratios of some features for each device. All data is anonymized. The subfolder **database** contains a database backup dump. This database was used in this program, and the functionality of this program is linked to this database. This folder also includes a schema of this database.

**demo** folder contains scripts to show the functionality of this program.

**src** contains the whole implementation of this tool. Subfolder **API** contains the specification of REST API. Folder **data_tools** includes functions to communicate with the database. It also provides some predefined SQL commands which are used in this program. Folder **similarity_search** contain implementation of similarity search.

Each folder contains *about.md* file, where is depicted the services and the functionality that each package provides.
Use:

1. Run src.main
2. Using the GET function:
    - for ***knn query***: /knn/<string: view>/<string: host>/<int: k>/<float: t> 
    eg. /knn/overall/239.36.249.160/5500/0.0003
If the address is not found, "IP not found" is displayed, otherwise the list of nearest addresses and their distance is displayed.

    - To display the ***address detail***, use / detail / <string: host> eg detail / 239.36.255.4
The address data is displayed if not found, IP not found is displayed.

    - for ***LOF*** query: / lof / <string: host> eg /lof/239.36.255.4
it is calculated and returns the LOF value for the address.

- > 1 outlier

- ~ 1 same as others

- <1 inlier
