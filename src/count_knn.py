import math
import json

from data_tools import dataCollector as collector
from similarity_search.similarity_search_main import knn_main

dc = collector.dataCollector()

addresses = dc.get_unique_ip_addresses()

for ip in addresses:
    ip = str(ip[0])
    knn = knn_main("overall", ip, math.inf, math.inf)
    dc.set_knn(ip, json.dumps(knn))

