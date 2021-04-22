# Host Behavior Similarity Search Tool
This tool was developed as part of my bachelor thesis. Its goal is to search for similar and different devices based on their communication profiles.

## Schema
- **Data** folder contains all the data that was used to test the tool. The folder itself contains two *.csv* files that contain raw communication profiles. The *host_profile_ratios_anon.csv* file contains the ratios of some features of a communication profiles. All data is anonymized. 
Subfolder **Database** contains a database backup dump. This database was used in this program, and the functionality of this program is linked to this database. 

- **Demo** folder contains scripts to show the functionality of this program.

- **Src** contains the whole implementation of this tool.
 ..* Subfolder **API** contains the specification of REST API. 
 ..* Subfolder **data_tools** includes functions to communicate with the database. It also provides some predefined SQL commands which are used in this program. 
 ..* Subfolder **similarity_search** contain implementation of similarity search.

Each folder contains *README.md* file, where is depicted the services and the functionality that each package provides.

## Use

### Pre-requisites

- PostgreSQL database v10.12
- Python v3.6
- Flask-RESTful package.

### Prepare

- **Load the database** using command (user postgres) 'psql db_host_profiles < data/database/db_dump.sql'

1. Run src.main ( on background )

2. Using the HTTP GET function:
    - ***K-NN query***: 
    Return K nearest neighbours to the given host.

      - / knn / view / host / k / t
      - view: One of 'overall', 'traffic' and 'application'. Default is 'overall'.
      - host: IP address of a specific host.
      - k: K value to determine how many devices should be in the result.
      - t: Threshold. Every device which is further than t is not included into the result.

    eg. /knn/overall/239.36.249.160/5500/0.0003

    If the address is not found, "IP not found" is displayed, otherwise the list of nearest addresses and their distance is displayed.


    - ***LOF query***: 
    Return value of a Local Outlier Factor for a specified device.

      - / lof / host / IP range 
      - host: IP address of a specific host.
      - IP range: IP range in which similar device will be searched.

    eg. / lof / 239.36.255.4 / 239.36.255

    ### LOF values interpetation:

    - \> 1 outlier

    - ~ 1 same as others

    - \< 1 inlier

    - ***Address Detail***:
    Shows a detail of a communication profile of a specified host.
      - / detail / host
      - host: IP address of a specific host.
    
    eg. detail / 239.36.255.4

    If the address is not found, "IP not found" is displayed, otherwise the communication profile is displayed.


Guide, how to use all functions of this program is described in the documentation.

The result is in the JSON format. 
