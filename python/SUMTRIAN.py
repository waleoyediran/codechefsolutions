from sys import stdin

__author__ = 'oyewale'


t = map(int, raw_input())
array = map(str, stdin.readlines())
# print array
arr = [map(int, str.split(array[x])) for x in range(len(array))]

# print arr

count = 0
# print(t[0])

for i in xrange(t[0]):
    # print "test case:" + str(i)
    le = arr[count][0]
    count += 1
    # print le

    # maxitem = [0 for x in range(le-1)]
    # maxitem = arr[le+count-1]
    # print maxitem
    # exit(0)
    for j in range(le+count-1, count-1, -1):
        # el = arr[j]
        # print el

        for k in range(len(arr[j])-1, -1, -1):
            if k != 0:
                ma = 0
                val = arr[j][k]
                val2 = arr[j][k-1]
                upper = arr[j-1][k-1]

                ma = max(val+upper, val2+upper)

                # print val
                # print upper;
                # print ma

                arr[j-1][k-1] = ma


        # print arr[j]
        # exit(0)
        # print j
    print arr[count][0]

    count += le