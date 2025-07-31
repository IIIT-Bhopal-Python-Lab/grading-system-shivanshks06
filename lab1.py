#function to determine grades
def grades(mark):
    mark = int(mark)  #convert input to integer
    if 90<=mark<=100:
        #check for A grade
        print("A")
    elif 75<=mark<=89:
        #check for B grade
        print("B")
    elif 60<=mark<=74:
        #check for C grade
        print("C")
    elif 40<=mark<=59:
        #check for D grade
        print("D")
    elif 0<=mark<=39:
        #check for F grade
        print("F")
    else:
        #if mark is invalid
        print("Invalid mark")

while True:  #infinite loop to take multiple inputs
        mark = input()   #taking input from user
        if mark == '-1':   #exit condition
            print("Exited successfully")
            break
        if mark.isdigit():  #check if input is a digit
            grades(mark)   #function call
        else:
            print("Invalid marks")
