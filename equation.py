def equation(a, b, c, d):
    if a == 0 and b == 0:
        return "INF"
    x = -b/a
    if c*x + d == 0:
        return "NO"

    return x


if __name__ == '__main__':
    print(equation(int(input()), int(input()), int(input()), int(input())))
