__author__ = 'oyewale'

### Solution Needs to be optimized ###
def main():
    T = int(raw_input())
    inpu = raw_input()
    solution = 0

    input_list = map(int, inpu.split())

    for i in range(T):
        index = i + 1
        while index < T:
            solution += input_list[i] & input_list[index]
            index += 1

    print solution


if __name__ == '__main__':
    main()
