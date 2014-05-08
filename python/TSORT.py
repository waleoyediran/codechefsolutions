from sys import stdin

__author__ = 'oyewale'


k = map(int, raw_input())

array = map(int, stdin.readlines())
array.sort()
# sor = list(set(array))
for i in xrange(len(array)):
    print array[i]
