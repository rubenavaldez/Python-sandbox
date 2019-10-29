truth = True
fakeNews = False

if truth:
    print("Truth was True")
elif fakeNews:
    print("This should never be true")
else:
    print("Nothing is true anymore")

x =0
y =1
z = 2


if x > y > z:
    print("x is greater than y is greater than z")
elif z>y or y>x:
    print("Z is greater than Y is greater than x")
else:
    print("It's over 90000!!")
