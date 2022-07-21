# BMI Calculator
# Enter your weight and height
# Using metrics of kg and cm
Weight = float(input("Enter your weight in kg:"))
Height = float(input("Enter your height in cm:"))
# Formula
bmi = (Weight / Height / Height) * 10000
print(f"Your BMI is {bmi}")
if bmi <= 18.5:
    print("You are underweight.\nTry implementing a healthy diet.")
elif 18.5 <= bmi < 24.9:
    print("You are at a normal weight.")
elif 25.0 <= bmi < 29.9:
    print("You are over weight.\nTry implementing exercise to your routine.")
elif 29.9 <= bmi < 34.9:
    print("You are at a obesity weight.\nTry implementing a healthy diet and exercise to your routine.")
else:
    print("Contact your doctor for further assistance.")
    
# Basal Metabolic Rate
print("Now let's calculate your basal metabolic rate.")
Age = int(input("Enter your age:"))
BMR1 = int(88.362 + (13.397 * Weight) + (4.799 * Height) - (5.677 * Age))
BMR2 = int(447.593 + (9.247 * Weight) + (3.09 * Height) - (4.330 * Age))
Id = str(input("Are you a Male or Female? (Male/Female)"))
if Id == "Male":
    print("Your BMR is =", BMR1)
elif Id == "Female":
    print("Your BMR is =", BMR2)
else:
    print("Error try again")
    quit()

