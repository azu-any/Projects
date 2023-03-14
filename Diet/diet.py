import sys
from tabulate import tabulate
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    figlet.setFont(font="ogre")
    print(figlet.renderText("Diet Controller"))


    print("\nWelcome! I will guide you to obtain your ideal daily intake of calories.\nLet's start with a few questions.")

    energy = tdee()
    print(f"\nThe calories you need are: {energy:.2f} kcal")
    cals = cal(energy)

    while True:
        try:
            print("\nHere are the recommended percentages of nutrients.\n")

            values = {("Carbohydrates:", "45-60%"),("Proteins:", "10-35%"), ("Fats:", "20-35%")}

            print((tabulate(values, headers=["Nutrients", "Recommended percentage"], tablefmt="fancy_grid")) + "\n")

            carbs_g, carbs_per = carbs(cals)
            prot_g, prot_per = prot(cals, carbs_per)
            fat_g, fat_per = fat(cals)

            if percent(carbs_per, prot_per, fat_per) == True:
                print("\nYou're good to go!")

                diet = [("Total Daily Energy Expenditure:", f"{energy:.2f} kcal"),
                        ("Calories you will consume:", str(cals) + " kcal"),
                        ("Carbohidrates:", str(carbs_g) + " g"),
                        ("Proteins:", str(prot_g) + " g"),
                        ("Fats:", str(fat_g) + " g")]

                print(tabulate(diet, tablefmt="double_grid"))

                print("\nYou can check the nutrients of some foods according to FAO at https://www.fao.org/3/y5022e/y5022e04.htm")
                sys.exit("\nSee you next time! :D")
            else:
                print("Your cabs, proteins and lipids are unbalanced")
                raise ValueError


        except ValueError:
            continue


# To get the Total Daily Energy Expenditure
def tdee():
    while True:
        try:
            weight = float(input("\nWhat's your weight in kg? ").strip())
            height = float(input("\nWhat's your height in cm? ").strip())
            age = int(input("\nWhat's your age? ").strip())
            sex = input("\nSelect your sex:\nF for Femenine or M for Masculine: ")

            print("\nHow much activity do you do? Select a number")
            print("1: I train less that 5 times a week\n2: I train 5 times a week between 1 and 2 hours\n3: I train 6 times a week for 2 hours")
            act = int(input().strip())

            if sex.casefold() == "f":
                match act:
                    case 1:
                        act = 1.5
                    case 2:
                        act = 1.64
                    case 3:
                        act = 1.9
                tee = act * (655 + (9.56 * weight) + (1.85 * height) - (4.7 * age))
                return tee

            elif sex.casefold() == "m":
                match act:
                    case 1:
                        act = 1.6
                    case 2:
                        act = 1.78
                    case 3:
                        act = 2.1
                tee = act * (66.4730 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age))
                return tee

            else:
                pass

        except ValueError:
            print("\nValue is not valid")
            continue

# To get the calores
def cal(energy):
    while True:
        try:
            print("\nThe previous result indicates how many calories you need to consume to stay as you are.")
            print("If you want to lose weight you can down your result, but not by more than 500 kcal\n")

            cals = float(input("How many calories would you like to consume daily? ").strip())

            if cals >= (energy - 500):
                print("\nNow, we need to define the percentages of carbs, proteins and fats.")
                print("The total sum of these porcentages should be: 100%")
                return cals
            else:
                print("Not enough calories")
                continue

        except ValueError:
            print("\nValue is not valid")
            continue

# To get carbs
def carbs(cals):
    while True:
        try:
            print("Recommended carbohydrates %: 45-60%")
            carbs_per = float(input("Carbs %: ").strip().strip("%"))
            if carbs_per >= 45 and carbs_per <=60:
                carbs_cal = float(carbs_per * cals / 100)
                carbs_g = carbs_cal /4
                print(f"You need {carbs_g:.2f} g of carbs")
                print(f"\nYou still have {100 - carbs_per}% for proteins and lipids\n")
                return (carbs_g, carbs_per)

            else:
                print("You need to consume at least 45% and at much 60%\n")
                continue

        except ValueError:
            print("\nValue is not valid")
            continue

# To get proteins
def prot(cals, per1):
    while True:
        try:
            print("Recommended proteins %: 10-35%")
            prot_per = float(input("Proteins %: ").strip().strip("%"))
            if prot_per >= 10 and prot_per <=35:
                prot_cal = float(prot_per * cals / 100)
                prot_g = prot_cal / 4
                print(f"You need {prot_g:.2f} g of proteins")
                print(f"\nYou still have {100 - per1 - prot_per}% for lipids\n")
                return (prot_g, prot_per)

            else:
                print("You need to consume at least 10% and at much 35%\n")
                continue

        except ValueError:
            print("\nValue is not valid")
            continue

# To get fats
def fat(cals):
    while True:
        try:
            print("Recommended fats %: 20-35%")
            fat_per = float(input("Fats %: ").strip().strip("%"))
            if fat_per >= 20 and fat_per <=35:
                fat_cal = float(fat_per * cals / 100)
                fat_g = fat_cal / 4
                print(f"You need {fat_g:.2f} g of fats\n")
                return (fat_g, fat_per)

            else:
                print("\nYou need to consume at least 20% and at much 35%\n")
                continue

        except ValueError:
                print("\nValue is not valid")
                continue

# To check percentage
def percent(carbs, prot, fat):
    if (carbs + prot + fat) == 100:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
