print("========= REGISTER ===============")
name = input("enter the name: ")

grade1 = float(input("enter the grade:"))
grade2 = float(input("enter the grade:"))
grade3 = float(input("enter the grade:"))

average = (grade1 + grade2 + grade3) / 3


# Validation grades high


if(grade1 >= grade2 and grade1 >= grade3):
    print(f"Highest grade: {grade1}")  

elif(grade2 >= grade1 and grade2 >= grade3):
     print(f"Highest grade: {grade2}")     

else:
    print(f"highest grade: {grade3}")      

# Validation grades lowest 


if(grade1< grade2 and grade1 < grade3):
    print(f"Lowest grade: {grade1}")      

elif(grade2 < grade1 and grade2 < grade3):
    print(f"Lowest grade: {grade2}")     

else:
    print(f"Lowest grade: {grade3}")   

# Situaation grade

if (average >= 7):
    print("Student Status: PASSED!")

elif (average > 5):
    print("Student Status: REMEDIAL!")

else:
    print("Student Status: FAILED!")

#validatiom grade









    
    
               