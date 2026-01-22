student_name = input("Enter student name: ")

score1 = int(input("Enter score for subject 1: "))
score2 = int(input("Enter score for subject 2: "))
score3 = int(input("Enter score for subject 3: "))

total = score1 + score2 + score3
average = total / 3

print("\n--- Student Result ---")
print("Name:", student_name)
print("Total Score:", total)
print("Average Score:", average)