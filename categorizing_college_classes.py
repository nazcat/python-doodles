classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

upper = []
lower = []

for i in classes:
    if int(i[-3:]) >= 300 and "MATH" in i:
        upper.append(i)
    elif int(i[-3:]) >= 200 and "ENG" in i:
        upper.append(i)
    elif int(i[-3:]) >= 400 and "PSYCH" in i:
        upper.append(i)
    else:
        lower.append(i)
        
print(upper)
print(lower)
