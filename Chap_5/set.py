# s = () # Empty set
# s = {} # don;t use {} as it will create as empty dictonary 

#  add and update

# s = {1,4,7,3,8,0,9} 
# # print(s , type(s))
# s.add(2)              #add single element
# s.update([11, 14])    #add multiple elements
# print(s)

# 
# 


# remove method
# s = {100, 5, 23, 999, 1, 42}
# s.remove(100)
# print(s)

# discard method

# s = {100, 5, 23, 999, 1, 42}
# s.discard(42)
# print(s)

# pop method : poping from left side 

# s = {4, 5, 7, 1 ,10}
# print(s)
# s.pop()
# s.pop()
# print(s)


#clear method : Clear all the sets

# s = {12 , 4, 56, 9}
# print(s)
# s.clear()
# print(s)


# Sets Operation

# Union:
# a = {1,2,3}
# b = {4,5,6}
# uni = a.union(b)
# print(uni)


# Intersection:
# a = {1,2,3,4}
# b = {4,5,6}
# inter = a.intersection(b)
# print(inter)


# Difference:

# c = {3,9,6,1}
# d = {25,9,0,3}
# diff = c.difference(d)
# print(diff)


# symetric Diffrence:

c = {3,9,6,1}
d = {25,9,0,3}

symdiff = c.symmetric_difference(d)
print(symdiff)

