import os

print("Demo 25.3.2020") 
print("239.36.99.8")
print("239.36.234.153")
print("239.36.249.175")
print("239.36.101.220")
print("239.36.36.36")
print("239.36.29.219")
print("239.26.29.75")
print("239.36.228.96")
print("239.36.109.218")
print()
print("KNN")
print("This utility provides a simple search for the nearest neighbours of the specified host.")
print("View are predefined weights assigned to each group of characteristics.")
print("Types of view are:")
print("-Overall - Each group of characteristics has the same weight.")
print("-Traffic - Traffic volume characteristics are prioritized.")
print("-Application - Application characteristics are prioritized.")
print("K-value specify number of nearest neighbours considered.")
print("Threshold sets the bound. Any host who is more than threshold is not considered.")
print("Eg. view: overall, host: 239.36.36.55, k: 5, t: 0.5\n")

n = False
while (not n):
    view = input("Insert view: ")
    host = input("Insert host ip address: ")
    k = input("Inser K-value: ")
    t = input("Insert threshold: ")
    command = "curl http://localhost:5000/knn/" + view + "/" + host + "/" + k + "/" + t
    print(command)
    os.system(command)
    choice = input("Do you want to enter different host? y/n\n")
    if choice == 'n':
        n = True

print("LOF")
print("Counts local outlier factor of specified host.")
print("Result less than 1 means inlier, more than 1 means outlier")
n = False
while(not n):
    host = input("Enter host ip address: ")
    command = "curl http://localhost:5000/lof/" + host
    print(command)
    os.system(command)
    choice = input("Do you want to enter diferrent host? y/n\n")
    if choice == 'n':
        n = True
print()
print("Detail")
print()
n = False
while not n:
    host = input("Insert host ip address: ")
    command = "curl http://localhost:5000/detail/" + host
    print(command)
    os.system(command)
    choice = input("Do you want to insert a different host? y/n\n")
    if choice == 'n':
        n = True

print()
print("Range search")
print()
print("This utility finds all devices closer than selected threshold")
n = False
while not n:
    host = input("Insert host ip address: ")  
    r = input("Insert range: ")
    command = "curl http://localhost:5000/range/" + host + "/" + r
    print(command)
    os.system(command)
    choice = input("Do you want to insert a different host? y/n\n")
    if choice == 'n':
        n = True


print("End of demo")
