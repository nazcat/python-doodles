yr = int(input("Enter year"))

if yr % 4 == 0:
    if yr % 400 == 0:
        print(str(yr) + " is a leap year.") 
    elif yr % 100 == 0:
        print(str(yr) + " is not a leap year.")
    else:
        print(str(yr) + " is a leap year.")
else:
    print(str(yr) + " is not a leap year.") 
