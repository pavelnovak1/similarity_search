from data_tools import dataCollector as collector
from similarity_search.similarity_search_main import knn_main

dc = collector.dataCollector()

addresses = dc.get_unique_addresses()

for ip in addresses:
    ip = str(ip[0])
    lof = lof_main(ip)
    dc.set_lof(ip, lof)
