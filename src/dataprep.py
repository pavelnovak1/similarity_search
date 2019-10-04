import counting_similarities

statistics = {}
NET = "147.250"
TD = 0          # Average duration of one flow
IB = 1          # Total number of input bytes
OB = 2          # Total number of output bytes
IP = 3          # Total number of input packets
OP = 4          # Total number of output packets
IF = 5          # Total number of input flows
OF = 6          # Total number of output flows
TCPP = 7        # Total number of TCP packets sent
TCPF = 8        # Total number of TCP flows sent
UDPP = 9        # Total number of UDP packets sent
UDPF = 10       # Total number of UDP flows sent
OTP = 11        # Total number of other protocol packets sent
OTF = 12        # Total number of other protocol flows sent
TP = 13         # Ports used
NUMBER_OF_FEATURES = 13

# nfdump -r nfcapd.201311200300_anon -o "fmt: %sa, %da, %td, %pr, %pkt, %byt, %sp, $dp" -N -q


def parsedata(file):
    """
    Parse data from file to new file
    :param file: File with nfdump data in format Source IP, Destination IP, Duration of flow, Protocol used,
    Number of packets in flow, Number of bytes in flow, Source port, Destination port

    Each line represents one flow
    :return: Nothing, creates new file called 'parsed' with parsed data
    """
    data = open(file, "r")
    parsed = open("parsed", "w")

    for record in data.readlines():
        parsed.write(record.replace(" ", "").replace("\t", "").replace("\n",",\n"))

    data.close()
    parsed.close()


def is_ip_in_network(ip):
    """
    Verify that IP address is in network defined in NET variable
    :param ip: IP address you want to verify
    :return: True if IP is in network, False if not
    """
    for i in range(len(NET)):
        if ip[i] != NET[i]:
            return False
    return True


def record_exists(ip):
    """
    Verify if statistics about given IP address is already in statistics database
    :param ip: IP address
    :return: True if already exists record about given IP, False otherwise
    """
    return ip in statistics


def init_new_record(ip):
    """
    Inits new record about IP address
    :param ip: IP address
    :return: Nothing, just creates new record in statistics database
    """
    statistics[ip] = [0 for _ in range(NUMBER_OF_FEATURES)]
    statistics[ip].append({})


def count_in_statistics(data):
    """
    Counts statistics about incoming traffic
    :param data: Record about one flow
    :return: Nothing, just updates statistics about incoming traffic and common statistics for both directions of flow
    """
    dstip = data.split(',')[1]
    if not record_exists(dstip):
        init_new_record(dstip)
    statistics[dstip] = update_in_stats(statistics.get(dstip), data)


def count_out_statistics(data):
    """
    Counts statistics about outcoming traffic
    :param data: Record about one flow
    :return: Nothing, just updates statistics about outcoming traffic and common statistics for both directions
    """
    srcip = data.split(',')[0]
    if not record_exists(srcip):
        init_new_record(srcip)
    statistics[srcip] = update_out_stats(statistics.get(srcip), data)


def total_flows(data):
    """
    Counts total number of flows in one statistics record
    :param data: Statistics about one IP
    :return: Total number of flows of that IP
    """
    return data[IF]+data[OF]


def update_ports(data, update, i):
    """
    Updates data about used ports
    :param data: Old statistics about IP
    :param update: New information about flow from/to this IP
    :param i: Swich, in for income flow, out for outcome flow
    :return: Updated statistics record
    """
    if i == "in":
        position = 7
    else:
        position = 6
    port = update.split(',')[position]
    if port in data[TP]:
        data[TP][port] += 1
    else:
        data[TP][port] = 1
    return data


def update_in_stats(data, update):
    """
    Updates statistics about income traffic for IP
    :param data: Old statistics record
    :param update: New information about flow
    :return: Updated statistics record
    """
    data[IF] += 1
    data[TD] = (data[TD]*(total_flows(data) - 1) + float(update.split(',')[2]))/(total_flows(data))
    data[IB] += int(update.split(',')[5])
    data[IP] += int(update.split(',')[4])
    data = update_ports(data, update, "in")
    if update.split(',')[3] == '6':
        data[TCPF] += 1
        data[TCPP] += int(update.split(',')[4])
    elif update.split(',')[3] == '17':
        data[UDPF] += 1
        data[UDPP] += int(update.split(',')[4])
    else:
        data[OTF] += 1
        data[OTP] += int(update.split(',')[4])
    return data


def update_out_stats(data, update):
    """
        Updates statistics about outcome traffic for IP
        :param data: Old statistics record
        :param update: New information about flow
        :return: Updated statistics record
        """
    data[OF] += 1
    data[TD] = (data[TD] * (total_flows(data) - 1) + float(update.split(',')[2])) / (total_flows(data))
    data[OB] += int(update.split(',')[5])
    data[OP] += int(update.split(',')[4])
    data = update_ports(data, update, "out")
    if update.split(',')[3] == '6':
        data[TCPF] += 1
        data[TCPP] += int(update.split(',')[4])
    elif update.split(',')[3] == '17':
        data[UDPF] += 1
        data[UDPP] += int(update.split(',')[4])
    else:
        data[OTF] += 1
        data[OTP] += int(update.split(',')[4])
    return data


def count_statistics(data):
    """
    Counts statistics for all IP addresses in network
    :param data: parsed data from nfdump
    :return: Nothing, just creates the statistics
    """
    for line in data.readlines():
        srcip = line.split(',')[0]
        dstip = line.split(',')[1]
        if is_ip_in_network(srcip):
            count_out_statistics(line)
        if is_ip_in_network(dstip):
            count_in_statistics(line)


print("Hello!")
parsedata("data")
print("Data parsed")
data = open("parsed", "r")
print("Counting statistics for hosts in network...")
count_statistics(data)
print('Done, statistics counted')
while True:
    host = input("Write a host: ")
    print("TD, IB, OB, IP, OP, IF, OF, TCPP, TCPF, UDPP, UDPF, OTP, OTF")
    print(statistics.get(host))
