def count_sort(a):
    try:
        n_list = list(map(int, a.split(' ')))
    except ValueError:
        return "ERROR!"

    min_n, max_n = 0, 100
    count_list = [0] * (max_n - min_n + 1)
    for el in n_list:
        if el > 100 or el < 0:
            return "ERROR!"
        count_list[el] += 1

    n_list = []
    for i in range(len(count_list)):
        j = 0
        while j < count_list[i]:
            n_list.append(i)
            j += 1

    return ' '.join(map(str, n_list))


if __name__ == '__main__':
    print(count_sort(input()))
