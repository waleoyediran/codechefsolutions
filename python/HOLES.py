__author__ = 'oyewale'


one = ['A', 'D', 'O', 'P', 'Q', 'R']
two = ['B']


t = int(raw_input())
for i in xrange(t):
    count = 0
    text = raw_input()
    li = list(text)

    for l in li:
        if l in one:
            count += 1
            continue
        if l in two:
            count += 2
    print count