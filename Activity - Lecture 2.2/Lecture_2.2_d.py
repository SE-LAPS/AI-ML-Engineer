sum = 0
count = 0

print("Enter a Series Of Numbers. Enter -999 to stop.")

while True:
    try:
        number = float(input(f"Enter Number {count + 1}: "))
        
        if number == -999:
            break
        
        sum += number
        count += 1
    except ValueError:
        print("Invalid Input. Please Enter a Number.")

if count > 0:
    print(f"\nSum of the {count} Numbers Entered: {sum}")
else:
    print("\nNo Numbers were Entered.")