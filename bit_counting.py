def bit_counting(a):
    count = 0
    while a > 0:
        if a % 2 == 1:
            count += 1
        a = a // 2

    return count


if __name__ == '__main__':
    print(bit_counting(int(input())))
