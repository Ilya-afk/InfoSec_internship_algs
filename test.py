from random import choice


# for i in range(n_village):
# distances.append(binary_search(shelters, villages[i]) + 1)

def UpperBound(shelters, key):
    left = -1
    right = len(shelters)
    while right > left + 1:
        middle = (left + right) // 2
        if shelters[middle][0] > key:
            right = middle
        else:
            left = middle

    if abs(shelters[left][0] - key) < abs(shelters[right][0] - key):
        return shelters[left][1]
    return shelters[right][1]


if __name__ == '__main__':
    a = []
    for i in range(100000):
        a.append(i)
    print(*a)
