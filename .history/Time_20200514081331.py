from HeaderFiles import Header1
import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
