import sys

l1 = []

print("Initial size:", sys.getsizeof(l1))

for i in range(20):
    l1.append(i)
    print(f"After inserting {i}: {sys.getsizeof(l1)} bytes")