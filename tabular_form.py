# Create a tuple of details of 5 students
students = (
    ("Ram", 25, "Male", "Computer Science"),
    ("Raju", 23, "Male", "Iski topi uske sar"),
    ("Babu", 100, "Male", "Batli"),
    ("Sham", 21, "Male", "Anuradha"),
    ("Anu", 22, "Female", "Robbery")
)

# Print out the details in tabular form
print("| Name   | Age | Gender | Field of Interest          |")
print("|--------|-----|--------|-------------------------|")
for student in students:
    print("| {:<6} | {:<3} | {:<6} | {:<23} |".format(student[0], student[1], student[2], student[3]))
