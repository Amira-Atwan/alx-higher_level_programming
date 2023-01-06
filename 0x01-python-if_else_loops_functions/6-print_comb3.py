#!/usr/bin/python3
for i in range(0, 8):
    for e in range(1, 10):
        if i != e and i < e:
            print('{}{}'.format(i, e), end=', ')
print('{}{}'.format(i + 1, e))
