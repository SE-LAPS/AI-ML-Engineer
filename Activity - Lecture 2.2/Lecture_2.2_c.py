def get_grade(mark):
    if mark > 75:
        return 'A'
    elif 65 <= mark <= 75:
        return 'B'
    elif 55 <= mark <= 64:
        return 'C'
    elif 45 <= mark <= 54:
        return 'S'
    else:
        return 'F'

marks = []
subjects = ['Maths', 'Science', 'English', 'History', 'Computer Science']

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter mark for {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Mark should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("\nGrades:")
for subject, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"{subject}: {mark} - Grade {grade}")

average_mark = sum(marks) / len(marks)
overall_grade = get_grade(average_mark)
print(f"\nAverage Mark: {average_mark:.2f}")
print(f"Overall Grade: {overall_grade}")