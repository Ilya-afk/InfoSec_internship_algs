def palindromes_counting(a):
    count = 0
    for i in range(1, a + 1):
        if str(i) == str(i)[::-1]:
            count += 1

    return count


if __name__ == '__main__':
    print(palindromes_counting(int(input())))
