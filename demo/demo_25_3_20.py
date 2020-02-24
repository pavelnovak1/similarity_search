import os

print("Demo 25.3.2020\n")
print("LOF\n")
host = input("Enter host ip address: ")
command = "curl http://localhost:5000/lof/" + host
print(command)
os.system(command)

