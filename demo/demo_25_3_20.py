import os

print("Demo 25.3.2020")
print("LOF")
n = False
while(not n):
    host = input("Enter host ip address: ")
    command = "curl http://localhost:5000/lof/" + host
    print(command)
    os.system(command)
    choice = input("Do you want to enter diferrent host? y/n")
    if choice == 'n':
        n = True

print("KNN")
n = False
while (not n):
    host = input("Enter host ip address: ")
    k = input("Enter K-value: ")
    command = "curl http://localhost:5000/knn/overall/"+host+"/"+k+"/0.5"
    print(command)
    os.system(command)
    choice = input("Do you want to enter different host? y/n")
    if choice == 'n':
        n = True

