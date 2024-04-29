from random import choice


def defense(n_village, villages, n_shelter, shelters):
    try:
        villages = list(map(int, villages.split(' ')))
        shelters = list(map(int, shelters.split(' ')))
    except ValueError:
        return "ERROR!"
    if n_village.isnumeric() and n_shelter.isnumeric():
        n_village, n_shelter = int(n_village), int(n_shelter)
    else:
        return "ERROR!"
    if n_village != len(villages) or n_shelter != len(shelters):
        return "ERROR!"

    distances = [0] * n_village
    for i in range(n_shelter):
        shelters[i] = [shelters[i], i]
    shelters = quicksort(shelters)

    for i in range(n_village):
        villages[i] = [villages[i], i]
    villages = quicksort(villages)

    distances = search(n_village, villages, n_shelter, shelters, distances)

    return ' '.join(map(str, distances))


def search(n_village, villages, n_shelter, shelters, distances):
    cur_border = 0
    for i in range(n_village):
        if cur_border + 1 == n_shelter:
            distances[villages[i][1]] = shelters[cur_border][1] + 1

        if cur_border + 2 == n_shelter:
            if (abs(villages[i][0] - shelters[cur_border + 1][0])
                    < abs(villages[i][0] - shelters[cur_border][0])):
                distances[villages[i][1]] = shelters[cur_border + 1][1] + 1
            else:
                distances[villages[i][1]] = shelters[cur_border][1] + 1

        for j in range(cur_border + 1, n_shelter):
            if (abs(villages[i][0] - shelters[j][0])
                    < abs(villages[i][0] - shelters[cur_border][0])):
                cur_border = j
            else:
                distances[villages[i][1]] = shelters[cur_border][1] + 1
                break

    return distances


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n[0] < q[0]:
                s_nums.append(n)
            elif n[0] > q[0]:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def binary_search(shelters, key):
    left = -1
    right = len(shelters)
    while right > left + 1:
        middle = (left + right) // 2
        if shelters[middle][0] > key:
            right = middle
        else:
            left = middle

    if right >= len(shelters):
        right -= 1
    if abs(shelters[left][0] - key) < abs(shelters[right][0] - key):
        return shelters[left][1]
    return shelters[right][1]


if __name__ == '__main__':
    print(defense(input(), input(), input(), input()))
