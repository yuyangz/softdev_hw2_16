#Jawad Kadir & Yuyang Zhang
#SoftDev2 pd07
#K16 -- Ready, Set, math!
#2018-04-26

#take x in a and take x from b that is not in a
def union(a,b):
    return [x for x in a +[ x for x in b if x not in a]]

print union([1,2,3],[3,5,6])

#take x that is both in a and b
def intersection(a,b):
    return [x for x in a if x in b]

print intersection([1,2,3],[2,3,4])
