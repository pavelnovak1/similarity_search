import data_tools.dbCommunicator as database

"""
This class contains elementary SQL commands using in this program.
"""


class dataCollector:

    def __init__(self):
        self.db = database.DBCommunicator()

    def host_get_raw_info(self, host):
        """
        Return raw host characteristics
        :param host : host_address
        :return Data about address
        """
        return self.db.dbexecute("SELECT * FROM host_profile WHERE hosts_ip_address =" + '\'' + host + '\'')

    def host_get_raw_info_directions(self, host, direction):
        """
        Return raw data about host in selected direction
        :param host host_address
        :param direction direction
        :return
        """
        return self.db.dbexecute("SELECT flows_sum, packets_sum, bytes_sum, flows_avg, packets_avg, bytes_avg, "
                                 "flows_max, packets_max, bytes_max FROM host_profile WHERE hosts_ip_address ="
                                 + '\'' + host + '\''
                                 + " AND direction = " + '\'' + direction + '\'')

    def host_get_raw_info_direction_in(self, host):
        return self.db.dbexecute("SELECT * FROM host_profile WHERE hosts_ip_adress =" + host + " AND direction=ín")

    def host_get_raw_info_direction_out(self, host):
        return self.db.dbexecute(
            "SELECT * FROM host_profile WHERE hosts_ip_adress =" + host + " AND direction='out'")

    def get_unique_ip_addresses(self):
        return self.db.dbexecute(
            "SELECT DISTINCT host_profile.hosts_ip_address FROM host_profile"
        )

    def get_host_profile(self, host):
        return self.db.dbexecute("SELECT * FROM profiles_both_directions_all_devices WHERE ip_address = '" + host + "'")

    def load_database_raw_data(self):
        return self.db.dbexecute("SELECT * FROM profiles_both_directions_all_devices")

    def general(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, communication_peers_avg_in, communication_peers_avg_out,"
                                 "flows_avg_in, flows_avg_out, packets_avg_in, packets_avg_out, bytes_avg_in, "
                                 "bytes_avg_out FROM profiles_both_directions_all_devices " + where_clause)

    def advanced(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, duration_50_in, duration_50_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def network(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, flows_sum_in, flows_sum_out, packets_sum_in, packets_sum_out,"
                                 "bytes_sum_in, bytes_sum_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, flows_stddev_in, flows_stddev_out, packets_stddev_in, "
                                 "packets_stddev_out, bytes_stddev_in, bytes_stddev_out,"
                                 "flows_95_in, flows_95_out, packets_95_in, packets_95_out,"
                                 "bytes_95_in, bytes_95_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def application(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, ports_avg_in, ports_avg_out, ports_min_in,"
                                 "ports_min_out, ports_max_in, ports_max_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def set_lof(self, host, lof):
        self.db.dbExecuteNoResult("INSERT INTO lof (ip_address, lof) VALUES ('" + host + "' , '" + str(lof) + "')")

    def set_knn(self, host, knn):
        self.db.dbExecuteNoResult(
            "INSERT INTO nearest_neighbours (ip_address, knn) VALUES ('" + host + "', '" + knn + "')")

    def get_knn(self, host):
        return self.db.dbexecute("SELECT knn FROM nearest_neighbours WHERE ip_address = '" + host + "'")
