# Prompt user for height and weight
userHeight = float(input("What is your height in meters? "))
userWeight = float(input("What is your weight in KG? "))

# Calculate BMI
BMI = userWeight / (userHeight ** 2)

# Determine BMI category and print the result
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are severely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

# Print the calculated BMI
print(f"Your BMI is {BMI:.2f}")
