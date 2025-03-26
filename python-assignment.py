first_number = int(input("Enter first number: "))
operator = input("Enter the Operator(+, -, *, /): ").strip()
second_number = int(input("Enter second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
    if operator == 0:
        print("Error. Zero is not a valid number for division")

print(f"{first_number} {operator} {second_number} = {result}")