correctAnswer = False

while correctAnswer == False:
    answer = input("What is 2 + 2?")
    if answer == "4":
        print("Correct!")
        correctAnswer = True
    else:
        print("Incorrect!")



verify = False
friendlies = []

while verify == False:
    yourName = input("What is your name?")
    print("We have",yourName," saved as your name.")
    verification = input("is this information correct?")
    if verification == "yes":
        verify = True
    

verifyTwo = False
while verifyTwo == False:
    addFriend = input("Would you like to add a new friend?")
    if addFriend == "yes":
        verifyThree = False
        while verifyThree == False:
            friendName = input("What is your friend's name?")
            print("We have",friendName," saved as your friend's name.")
            verificationTwo = input("is this information correct?")
            if verificationTwo == "yes":
                verifyThree = True
                friendlies.append(friendName)
    else:
        verifyTwo = True


print(yourName,", we have successfuly added your friends:")

i = 0
while i < len(friendlies):
    print(friendlies[i])
    i += 1