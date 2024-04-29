def oil_analysis(a):
    try:
        info_list = list(map(int, a.split(' ')))
    except ValueError:
        return "ERROR!"

    n, a, b = info_list[0:3]
    price = []
    for i in range(4, len(info_list), 2):
        price.append([info_list[i - 1], info_list[i]])

    if len(price) != n:
        return "ERROR!"

    min_cost1 = [1000, 1000]
    min_cost2 = [1000, 1000]
    for cost in price:
        if cost[0] < min_cost1[0]:
            min_cost1[0] = cost[0]
        elif cost[1] < min_cost1[1]:
            min_cost1[1] = cost[1]
        if cost[1] < min_cost2[1]:
            min_cost2[1] = cost[1]
        elif cost[0] < min_cost2[0]:
            min_cost2[0] = cost[0]

    answer = max(round(a / min_cost1[0] + b / min_cost1[1], 2),
                 round(a / min_cost2[0] + b / min_cost2[1], 2))
    return f'{answer:.2f}\n'


if __name__ == '__main__':
    print(oil_analysis(input()))
