from Process import Process

p1 = Process("P1", 1, [2, 3])
p2 = Process("P2", 2, [3, 1, 2])
p3 = Process("P3", 4, [2, 2])
p4 = Process("P4", 6, [3, 1])

calls = [p1.call, p2.call, p3.call, p4.call]

# print(calls[3])  # devuelve el 6

for i in range(calls[3]):
    print(i)