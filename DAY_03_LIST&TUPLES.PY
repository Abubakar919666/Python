# LIST IN PYTHON

student  = ["Ali ", "muhammad", "bakar", "fahemm" ]
print(student[0])

# LIST SLICING (LIST KA TUKRA MIL JATA HE )

mark  = [14, 15, 16, 11]
print(mark[0:2])
print (student[0:2])

# LIST METHOD IN PYTHON

rollNumber = [14, 15, 16, 11, 10 ]

# append()  method
rollNumber.append(12)
print(rollNumber)

# sort() method (accending order)
rollNumber.sort()
print(rollNumber)

# sort(reverse(true)) method (decending order)
rollNumber.sort(reverse=True)
print(rollNumber)

# reverse()  method
rollNumber.reverse()
print(rollNumber)         

# insert() method
rollNumber.insert(3, 13)
print(rollNumber)

# pop() method
rollNumber.pop(6)
print(rollNumber)

# remove() method
rollNumber.remove(15)
print(rollNumber)