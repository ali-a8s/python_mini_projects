def calculate_bmi(height_m, weight_kg):
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def bmi_calculator():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters (e.g. 1.75): "))

            if height > 3: 
                print(f"Height {height}m is impossible! Did you mean {height/100:.2f}m?")
                confirm = input("Type 'y' to auto-convert from cm, or anything else to re-enter: ")
                if confirm.lower() == 'y':
                    height /= 100
                else:
                    continue

            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers.")
                continue

            bmi = calculate_bmi(height, weight)
            category = bmi_category(bmi)

            print(f"\nYour BMI is {bmi:.1f}")
            print(f"Category: {category}\n")
            break

        except ValueError:
            print("Please enter valid numbers!")


print("BMI Calculator")
while True:
    choice = input("Ready to calculate? [y/n]: ").strip().lower()
    if choice == 'y':
        bmi_calculator()
    elif choice == 'n':
        print("Alright, see you later!")
        break
    else:
        print("Just type 'y' or 'n' dude.")