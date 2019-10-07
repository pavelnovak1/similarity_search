import counting_similarities
import dataprep

"""
Hlavni funkce ktera postupne spocita statistiky, a nasledne na zaklade zadanych kriterii spocita nejblizsi hosty
"""


def main():
    data = dataprep.main("data")
    while True:
        host = input("Write a host: ")
        t = int(input("Minimal threshold: "))
        knn = int(input("K nearest neighbours: "))
        print("Counting similar hosts for " + host)
        result = counting_similarities.main(data, host, t, knn)
        if len(result) == 0:
            print("Network " + host + " was not found or no address satisfies threshold ", str(t))
            return 0
        print("Number of addresses found on network ", host, ": ", len(result))
        for IP, hosts in result.items():
            print("IP - " + IP)
            print(data[IP])
            print()
            for simIP, d in hosts:
                print("Similar host: " + simIP + " in distance: " + str(d))
                print(data[simIP])
                print()

            if len(hosts) == 0:
                print("Threshold " + str(1000) + " is too big. No addresses satisfied")
            print()
            print("_________________________________________________________")


if __name__ == "__main__":
    main()
