# STRING FUNCTION 

# 1) endswith() function
str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr
print(str.endswith("er."))

# 2) capitalize() function

str = "i am a coder."
str = str.capitalize()
print(str)

# 3) replace(old,new)

str = "i am a coder."
print(str.replace("o","a"))

# 4) find()


str = "i am a coder."
print(str.find("coder"))




# Conditional statement
light = "yellow"
if (light == "red"):
    print("stop this")
elif (light == "green"):
    print("go")
else:
    print("then wait")