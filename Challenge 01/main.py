print("========================================")
name = input("enter the name: ")


note1 = float(input("enter the first note: "))
note2 = float(input("enter the second note: "))
note3 = float(input("enter the third note: "))

average = (note1 + note2 + note3) / 3

print(" ======= resultados ========= ")
print(f"Name: {name}")
print(f"Average note: {average}")


if average >= 7:
    print("Results: Approved!!")   

elif average < 6.9 and average> 5:
    print("Results: Recuperation!!")

else:
    print("Results: Reproved!!")





"""
if(note1, note2,note3 < 0 or note1, note2,note3 > 10):
        print(" Syntax Invalide !!! ")
else:
    True
"""