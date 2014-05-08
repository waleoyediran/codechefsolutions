from sys import stdin

__author__ = 'oyewale'


def main():
    inp = stdin.readline()
    arr = str.split(inp)

    amount = int(arr[0])
    balance = float(arr[1])
    charge = 0.50

    if (amount + charge) > balance:
        pass
    elif (amount % 5) != 0 :
        pass
    else:
        balance -= amount + charge

    print ("{0:.2f}".format(balance))



if __name__ == '__main__':
    main()

