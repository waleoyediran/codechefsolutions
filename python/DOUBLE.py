__author__ = 'oyewale'

def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        if N%2 == 0:
            print N
        else:
            print N-1

if __name__ == '__main__':
    main()
