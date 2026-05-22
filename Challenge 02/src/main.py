import os
from utils.functions import get_grades
from utils.functions import process_grade
from utils.functions import get_status
from utils.functions import validation_grade

print("======== FORM ===========")

name = input("Enter the name: ")
grade = validation_grade()
grades = get_grades()
average, highest, lowest = process_grade(grades)

os.system("cls")
print("========= RESULTS =========")
print(f"yout name is {name}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

get_status(average)