marks = int(input("Enter a marks"))

if marks>=81 and marks<=100:
    print("Very Good")
elif marks<=80 and marks>=61:
    print("Good")
elif marks>=40 and marks<=60:
    print("Average")
else:
    print("Fail")

