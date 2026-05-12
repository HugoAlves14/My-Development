def validation_grade():
    while True:
        grade = float(input("Enter the grade: "))

        if(grade >= 0 and grade <= 10):
            return grade
        else:
            print("Invalide Grade! Try again!") 


def get_grades():

    grades = []

    for i in range(3):
        grade = validation_grade()
        grades.append(grade)

    return grades


def process_grade(grades):

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return average,highest,lowest


def get_status(average):
    if(average >= 7):
        print("Status Student: PASSED!")
    
    elif(average >= 5):
        print("Status Student: REMIED!")

    else:
        print("Status Student: Failed")
