import data_tools.db_connection as database


class sql_commands:
    """
    This class contains predefined SQL commands used in this program.
    """

    def __init__(self):
        """
        Connection to the database using db_connection class.
        """
        self.db = database.db_connection()

    def get_unique_ip(self):
        """
        Return all unique IP addresses in database.
        :return: Unique IP addresses.
        """
        return self.db.get_data("SELECT DISTINCT hosts_ip_address "
                                "FROM host_profile")

    def load_database_range(self, ip_range):
        """
        Return communication profiles of all devices in a specified IP range.
        :param ip_range: IP range from which the communication profiles will be selected.
        :return: Communication profiles of all devices in a specified IP range.
        """
        return self.db.get_data("SELECT * "
                                "FROM final_profiles "
                                "WHERE ip_address LIKE '{}%';"
                                .format(ip_range))

    def get_ip_range(self, ip_range):
        """
        Return all unique IP addresses in a specified IP range.
        :param ip_range: IP range from which the addresses will be selected.
        :return: Unique IP addresses from the specified IP range.
        """
        return self.db.get_data("SELECT DISTINCT ip_address "
                                "FROM final_profiles "
                                "WHERE ip_address LIKE '{}%';"
                                .format(ip_range))

    def get_host_profile(self, host):
        """
        Return the normalized communication profile of the specified host.
        :param host: Wanted host.
        :return: The communication profile of the specified host.
        """
        return self.db.get_data("SELECT * "
                                "FROM final_profiles "
                                "WHERE ip_address = '{}';"
                                .format(host))

    def host_get_raw_info(self, host):
        """
        Return the communication profile of a specified host before normalization.
        :param host : Wanted host.
        :return The communication profile of a specified host before normalization.
        """
        return self.db.get_data("SELECT * "
                                "FROM host_profile "
                                "WHERE hosts_ip_address = '{}';"
                                .format(host))

    def host_get_raw_info_directions(self, host, direction):
        """
        Return the communication profile of a specified host in a specific direction.
        Communication profile is before normalization process.
        :param host : Wanted host.
        :param direction : Wanted direction.
        :return The communication profile of a specific host in a specific direction.
        """
        return self.db.get_data("SELECT flows_sum, packets_sum, bytes_sum, flows_avg, packets_avg, bytes_avg, "
                                "flows_max, packets_max, bytes_max "
                                "FROM host_profile "
                                "WHERE hosts_ip_address = '{0}' "
                                "AND "
                                "direction = '{1}';"
                                .format(host, direction))

    def profiles_categories(self, ip_range, ip=None):
        """
        Return communication profiles aggregated into the view categories.
        Can return both for a single IP address and the specific IP range.
        :param ip_range: Wanted IP range.
        :param ip: Wanted host. If not specified, result for whole IP range is returned.
        :return: The aggregatetd communication profiles for a single host or IP range.
        """
        if ip is not None:
            where = "WHERE ip_address = '{}';".format(ip)
        else:
            where = "WHERE ip_address LIKE '{}%';".format(ip_range)
        return self.db.get_data("SELECT * "
                                "FROM categories {}"
                                .format(where))

    def get_quantiles(self, ip_range):
        """
        Return Q1, Q2 and Q3 of distances between devices in a specified IP range.
        :param ip_range: Wanted IP range.
        :return: Quantiles of distances between devices in a specified IP range.
        """
        return self.db.get_data("SELECT q1, q2, q3 "
                                "FROM quantiles "
                                "WHERE ip_range = '{}'"
                                .format(ip_range))

    def update_quantiles(self, ip_range, q1, q2, q3):
        """
        Insert or update quantiles for a specified IP range.
        :param ip_range: Wanted IP range.
        :param q1: First quantile. Q1.
        :param q2: Second quantile. Q2.
        :param q3: Third quantile. Q3.
        :return: Nothing. Just update the record.
        """
        return self.db.insert_data("INSERT INTO quantiles(ip_range, q1, q2, q3) "
                                   "VALUES('{0}', '{1}', '{2}', '{3}' ) "
                                   "ON CONFLICT (ip_range) "
                                   "DO UPDATE "
                                   "SET q1 = {1}, q2 = {2}, q3 = {3};"
                                   .format(ip_range, str(q1), str(q2), str(q3)))
