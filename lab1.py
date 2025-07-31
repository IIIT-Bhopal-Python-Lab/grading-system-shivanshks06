mark = int(input())  # input
if 90 <= mark <= 100:  #check for A grade
    print("A")
elif 75 <= mark<= 89:   #check for B grade
    print("B")
elif 60 <= mark <= 74:   #check for C grade
    print("C")
elif 40 <= mark <= 59:   #check for D grade
    print("D")
elif 0 <= mark <= 39:   #check for F grade
    print("F")
else:
    print("Invalid mark")
