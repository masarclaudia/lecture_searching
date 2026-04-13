
from generators import ordered_sequence, unordered_sequence
from searching import linear_search, binary_search
import time
import random
import matplotlib.pyplot as plt

seq = ordered_sequence(50)
print(seq)

times_linear = []
times_binary = []
ns = list(range(100, 10000, 1000))


for n in ns:
    seq = unordered_sequence(n)
    target = random.choice(seq)

    sorted_seq = sorted(seq)

    start = time.perf_counter()
    res1 = linear_search(seq, target)
    end = time.perf_counter()

    times_linear.append(end - start)

    print("Linear search výsledek: ", res1)
    print("Linear search čas: ", end - start)


    start = time.perf_counter()
    res2 = binary_search(sorted_seq, target)
    end = time.perf_counter()

    times_binary.append(end - start)

    print("Binary search výsledek: ", res2)
    print("Binary search čas: ", end - start)


sizes = ns

plt.plot(sizes, times_linear, marker="o", label="Lineárne vyhľadávanie")
plt.plot(sizes, times_binary, marker="o", label="Binárne vyhľadávanie")

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.legend()
plt.grid()
plt.show()