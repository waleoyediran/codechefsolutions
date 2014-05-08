from sys import stdin

__author__ = 'oyewale'


def main():
    n, k = map(int, stdin.readline().split())
    d = 0
    array = map(int, stdin.readlines())

    for i in range(len(array)):
        if array[i] % k == 0:
            d += 1
    print d



if __name__ == '__main__':
    main()
