def cow_dung(n, throws):
    try:
        throws = list(map(int, throws.split(' ')))
    except ValueError:
        return "ERROR!"
    if n.isnumeric():
        n = int(n)
    else:
        return "ERROR!"
    if n != len(throws):
        return "ERROR!"

    max_throw = [0, 0]
    vasily_throw = 0
    answer = 1
    for i in range(n):
        if throws[i] > max_throw[0]:
            max_throw = [throws[i], i]

    for i in range(1, n - 1):
        if (str(throws[i])[-1] == '5' and max_throw[1] < i and
                throws[i+1] < throws[i] and throws[i] > vasily_throw):
            vasily_throw = throws[i]
    for throw in throws:
        if throw > vasily_throw:
            answer += 1

    if vasily_throw:
        return answer
    return 0


if __name__ == '__main__':
    print(cow_dung(input(), input()))
