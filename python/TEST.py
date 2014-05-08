import fileinput

__author__ = 'oyewale'


def main():
    for line in fileinput.input():
        if int(line) != 42:
            print line
        else:
            return


if __name__ == '__main__':
    main()
