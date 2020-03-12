import data_tools.dbCommunicator as database
import data_tools.dataCollector as collector

db = database.DBCommunicator()
dc = collector.dataCollector()

addresses = dc.get_unique_ip_addresses()
for ip in addresses:
    db.dbExecuteNoResult("ALTER TABLE knn_matrix ADD COLUMN " + ip + " double precision;")
for ip in addresses:
    db.dbExecuteNoResult("INSERT INTO knn_matrix (ip) VALUES (" + ip + ");")
for host in addresses:
    nearest_neighbours = dc.get_knn(host)[0][0]
    for h, d in nearest_neighbours.items():
        db.dbExecuteNoResult("UPDATE table_name SET " + h + " = " + d + " WHERE ip = " + host + "; ")
