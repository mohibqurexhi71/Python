# a = () #The Empty tuple
# a= (1,)
# print(a , type(a))
# a = (1, 334, 2,23 , 2, False , "Rohan" ," Shivam")
# print(a)
# a[0] = 345 #x we do not change becouse Immutable
# print(a)
# print(type(a))

# Tuple Methods

# a = (1, 334,45, 2,23 , 2, False , "Rohan" ," Shivam")
# print(a)
# repetation = a.count(2)
# print("Repeted NUmber",repetation)

# # location
# loc = a.index(2)
# print(f"Located at {loc} index")

# we can check if an item is exist in our tuple using 'in' function
# my_tuple = {1,2,3}
# print(2 in my_tuple)
# print(4 in my_tuple)
 
# Excercise
# 1.
# fruits = []
# f1 = input('Enter Your Favorite Fruits');
# fruits.append(f1)
# f2 = input('Enter Your Favorite Fruits');
# fruits.append(f2)
# f3 = input('Enter Your Favorite Fruits');
# fruits.append(f3)
# f4 = input('Enter Your Favorite Fruits');
# fruits.append(f4)
# f5 = input('Enter Your Favorite Fruits');
# fruits.append(f5)
# print(fruits)


# 2.
# wrong method to do 
# marks = []
# f1 = input('Enter Marks here: ');
# marks.append(f1)
# f2 = input('Enter Marks here: ')
# marks.append(f2)
# f3 = input('Enter Marks here: ')
# marks.append(f3)
# f4 = input('Enter Marks here: ')
# marks.append(f4)
# f5 = input('Enter Marks here: ')
# marks.append(f5)
# f5 = input('Enter Marks here: ')
# marks.append(f5)
# marks.sort()
# print(marks)

# Right method
# marks = []
# f1 = int(input('Enter Marks here: '))
# marks.append(f1)
# f2 = int(input('Enter Marks here: '))
# marks.append(f2)
# f3 = int(input('Enter Marks here: '))
# marks.append(f3)
# f4 = int(input('Enter Marks here: '))
# marks.append(f4)
# f5 = int(input('Enter Marks here: '))
# marks.append(f5)
# f5 = int(input('Enter Marks here: '))
# marks.append(f5)
# marks.sort()
# print(marks)
# int is imortant otherwise the input take in the form of charecter  and it compare two value like this : 566 > 6  that means python sorts strings alphabetially not numerically

# 3.
# a = (1,2,"Harry")
# a[2] = "Larry" # x Not chnanged
# print(a)

# 4. 

# l = [23, 44, 34,56]
# print(sum(l))

# # 5.
# l = [7,8,0,0,9]
# print(l.count(0))


