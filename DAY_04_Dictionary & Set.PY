# DICTIONARIES IN PYTHON 

dic = {
    "name": "abubakar",
    "age" : 19,
    "class": "uni",
    "Uni_Name":"ku"
}

print(dic)
print(dic.keys())

# Nested dic in python 

nested_dic = {
    "name": "abubakar",
    "age" :{
        "age_day": "friday",
        "age_month": "april" 
    },
    "class": "uni",
    "Uni_Name":"ku"
}

print(nested_dic)

# Method in dictionaries

# value() method 
# items() method 
# get()  method 
# update() method

# SETS IN PYTHON 
collection = {1, 4, 6, 8, 9, 10}
print(collection)
print(type(collection))
# set doblicate value ignore
# set are mutable but the element are immutable


# Methods in sets

# Add method 
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)


#remove method 
collection.remove(1)
print(collection)

#pop method 
collection = {3, 4, 6 }
print(collection.pop())

#Union method 
set1 = {2, 3, 5, 6, 7, 8}
set2 = {9, 10, 5, 6, 1, 8}
print(set1.union(set2))

#intersection method 
print(set1.intersection(set2))