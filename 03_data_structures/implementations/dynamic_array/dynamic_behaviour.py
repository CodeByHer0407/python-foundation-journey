import sys

l1 = []

print("Initial size:", sys.getsizeof(l1))

for i in range(20):
    l1.append(i)
    print(f"After inserting {i}: {sys.getsizeof(l1)} bytes")


c = "python"
print(c[:-1])

l1 = [12, 31, 14, 51]
print(l1.pop())
print(l1)

## Indexing behavior

print(l1[1])