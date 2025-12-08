pass_mark = 45
passed = 0
failed = 0

student_scores = float(input("Enter the scores of 15 students:"))



for x in range(1, 15 + 1):

    while True:
        try:
            score = float(input(f"Score of student {x}: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    if score >= pass_mark:
        passed += 1
    else:
        failed += 1

print("\nRESULTS")
print("Number of students who passed:", passed)
print("Number of students who failed:", failed)


