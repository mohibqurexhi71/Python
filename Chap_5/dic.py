# Dictionary

marks = {
    "Mohib": 100,
    "Harry": 99,
    "Shubam":34
}
# print(marks,type(marks))
# print(marks["Harry"])
# print(marks.keys())
# print(marks.values())
# print(marks.items())

# Updation of Dict

# marks.update({"Mohib": 99, "Renuka": 88})
# print(marks)

# get method
# print(marks.get("Harry"))
# print(marks.get("Renuka")) # Give None
# print(marks["ajmal"]) #Give Error


# pop Method

# remover = marks.pop("Shubam")
# print(marks)
# print(remover)

# clear Method : Remove all items

clear = marks.clear()
print(marks)

# pop item

# remove  = marks.popitem()
# marks.popitem()
# print(marks)