marks = []

for i in range(10):
    while True:
        try:
            mark = float(input(f"Enter mark for student {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Mark should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / len(marks)

print(f"\nMaximum mark: {max_mark}")
print(f"Minimum mark: {min_mark}")
print(f"Average mark: {avg_mark:.2f}")