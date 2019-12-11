import src.dbCommunicator as database


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
        return self.db.dbexecute("SELECT * FROM host_profile WHERE hosts_ip_adress =" + address + " AND direction=Ã­n")

    def get_out_info_about_address(self, address):
        return self.db.dbexecute(
            "SELECT * FROM host_profile WHERE hosts_ip_adress =" + address + " AND direction='out'")

    def get_unique_addresses(self):
        return self.db.dbexecute(
            "SELECT DISTINCT host_profile.hosts_ip_address FROM host_profile"
        )

    def get_host_profile(self, host):
        data = self.db.dbexecute("SELECT * FROM host_profiles_final WHERE hosts_ip_address = '" + host + "'")
        return data

    def get_all_profiles(self):
        return self.db.dbexecute("SELECT * FROM host_profiles_final")
