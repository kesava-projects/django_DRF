def find_odd(fn):
    def wrapper():
        lis = fn()
        print("Odd numbers:")
        for li in lis:
            if li % 2 != 0:
                print(li)
        return lis
    return wrapper

def find_even(fn):
    def wrapper():
        lis = fn()
        print("Even numbers:")
        for li in lis:
            if li % 2 == 0:
                print(li)
        return lis
    return wrapper

@find_odd
@find_even
def main():
    lis = [1, 2, 3, 5, 6]
    return lis

def find_sum(fn):
    def wrapper():
        lis, tar = fn()
        print("Sum of numbers:")
        count = 0
        for li in lis:
            if li == tar:
                count += 1
        print(tar * count)
    return wrapper




@find_sum
def find_numbers():
    lis = [1, 24, 12, 56, 68, 7, 7, 7, 24, 56, 68, 24, 7]
    target = 56
    return lis, target

if __name__ == '__main__':
    main()
    find_numbers()

