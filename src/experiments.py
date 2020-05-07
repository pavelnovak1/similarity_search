from similarity_search.similarity_search_main import lof_main as lof
import time

def lof_dependency_on_k(k_max):
    for i in range(1,k_max):
        start = time.time()
        l = lof("239.36.249.81", "239.36.249", i)
        end = time.time()
        print("K: " + str(i))
        print("Time: " + str(end - start))
        print("LOF: " + str(l))
        print()

lof_dependency_on_k(20)
