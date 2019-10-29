# def printSomething(thing):
#     print(thing)

# printSomething("Hello There")

def printSomething(word = "dog", number = "5"):
    print("word ",word)
    print("number ", number)

# printSomething(word= "cat", number= 7)


def printManyThings(*things):
    for thing in things:
        print(thing)

printManyThings("dog","cat","pig","mouse","rabbit")