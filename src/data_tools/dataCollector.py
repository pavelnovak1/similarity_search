import src.data_tools.dbCommunicator as database


class dataCollector:

    def __init__(self):
        self.db = database.DBCommunicator()

    def get_info_about_address(self, address):
        return self.db.dbexecute("SELECT * FROM host_profile WHERE hosts_ip_address =" + '\'' + address + '\'')

    def get_data_about_host(self, host, direction):
        return self.db.dbexecute("SELECT flows_sum, packets_sum, bytes_sum, flows_avg, packets_avg, bytes_avg, "
                                 "flows_max, packets_max, bytes_max FROM host_profile WHERE hosts_ip_address ="
                                 + '\'' + host + '\''
                                 + " AND direction = " + '\'' + direction + '\'')

    def get_in_info_about_address(self, address):
        return self.db.dbexecute("SELECT * FROM host_profile WHERE hosts_ip_adress =" + address + " AND direction=ín")

    def get_out_info_about_address(self, address):
        return self.db.dbexecute(
            "SELECT * FROM host_profile WHERE hosts_ip_adress =" + address + " AND direction='out'")

    def get_unique_addresses(self):
        return self.db.dbexecute(
            "SELECT DISTINCT host_profile.hosts_ip_address FROM host_profile"
        )

    def get_host_profile(self, host):
        data = self.db.dbexecute("SELECT * FROM profiles_both_directions_all_devices WHERE ip_address = '" + host + "'")
        return data

    def get_all_profiles(self):
        return self.db.dbexecute("SELECT * FROM profiles_both_directions_all_devices")

    def get_general_statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, communication_peers_avg_in, communication_peers_avg_out,"
                                 "flows_avg_in, flows_avg_out, packets_avg_in, packets_avg_out, bytes_avg_in, "
                                 "bytes_avg_out FROM profiles_both_directions_all_devices " + where_clause)

    def get_advanced_statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, duration_50_in, duration_50_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def get_network_layer_statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, flows_sum_in, flows_sum_out, packets_sum_in, packets_sum_out,"
                                 "bytes_sum_in, bytes_sum_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def get_statistic_features_statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, flows_stddev_in, flows_stddev_out, packets_stddev_in, "
                                 "packets_stddev_out, bytes_stddev_in, bytes_stddev_out,"
                                 "flows_95_in, flows_95_out, packets_95_in, packets_95_out,"
                                 "bytes_95_in, bytes_95_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

    def get_application_layer_statistics(self, exc=None, host=None):
        if exc is not None:
            where_clause = "WHERE ip_address != '" + exc + "'"
        else:
            where_clause = "WHERE ip_address = '" + host + "'"
        return self.db.dbexecute("SELECT ip_address, ports_avg_in, ports_avg_out, ports_min_in,"
                                 "ports_min_out, ports_max_in, ports_max_out FROM "
                                 "profiles_both_directions_all_devices " + where_clause)

