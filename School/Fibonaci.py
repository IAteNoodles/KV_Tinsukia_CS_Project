def fibonaci(num: int):
    a, b = 0, 1
    count = 2
    while True:
        print(a)
        print(b)
        a = b + a
        count += 1
        if count == num:
            print(a)
            break
        b = a + b
        count += 1
        if count == num:
            print(a)
            print(b)
            break


def fibonaci_test(num: int):
    i, f, s = 0, 0, 1
    while True:
        if i <= 1:
            next = i
        else:
            next = f + s
            f = s
            s = next
        if next > num:
            break
        print(next)
        i = i + 1


if __name__ == '__main__':
    fibonaci_test(int(input("Enter The Limit: ")))
