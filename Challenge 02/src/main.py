import os
from utils.functions import get_grades
from utils.functions import process_grade
from utils.functions import get_status

print("======== FORM ===========")
grades = get_grades()
average, highest, lowest = process_grade(grades)

os.system("cls")
print("========= RESULTS =========")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

get_status(average)