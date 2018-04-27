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

#takes x in a that is not in b
def set_difference(a,b):
    return [x for x in a if x not in b]

print set_difference([1,2,3],[2,3,4])

#takes x in a that is not in b and x in b that is not in a
def sym_difference(a,b):
    return set_difference(a,b)+ set_difference(b,a)

print sym_difference([1,2,3],[2,3,4])

#pairs up each x in a and each x in b
def cart_prod(a,b):
    return [(x,y) for x in a for y in b]

print cart_prod([1,2,3],[2,3,4])
