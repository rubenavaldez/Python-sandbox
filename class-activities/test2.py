arr = [1,2,3]


arr.append(4)


arr[0] = 5

#print("First element of arr is   {0}".format(arr[0]))


a,b = [1,2]

#print("a: ",a,"b:",b)

student = {
    "firstname" : "Eric",
    'lastname': "Rosas"
}
#print(student.get("firstname"))

#print(student.keys())
#print(student.values())

for key in student:
    print("The key {0} has a value of {1}".format(key,student[key]))

