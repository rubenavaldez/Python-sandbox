arr = []

def createObj(given, sur):
    return {
        "first": given,
        "last": sur
    }

def verify():
    global addMore
    resp = input("Yes or no? ")
    if resp.lower() == 'yes' or resp.lower() == 'y':
        addMore = True
    else:
        addMore = False

addMore = True

while addMore == True:
    print("Would you like to add a student? ")
    verify()
    if addMore == False:
        break
    a = input("What's the first name? ")
    b = input("Whats the last name? ")
    arr.append(createObj(a,b))


print("Here's the list of students: ")
for key in arr:
    print(key.get("first"), key.get("last"))