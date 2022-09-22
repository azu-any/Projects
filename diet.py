def main():
    energy = tdee()
    cals = cal(energy)
    carbs_g, carbs_per = carbs(cals)
    prot_g, prot_per = prot(cals, carbs_per)
    fat_g, fat_per = fat(cals)

    if percent(carbs_per, prot_per, fat_per) == True:
        pass
    else:
        print("Your cabs, proteins and lipids are unbalanced")
        carbs_g, carbs_per = carbs(cals)
        prot_g, prot_per = prot(cals, carbs_per)
        fat_g, fat_per = fat(cals)



# To get the Total Daily Energy Expenditure
def tdee():
    while True:
        try:
            weight = float(input("What's your weight in kg? ").strip())
            height = float(input("What's your height in cm? ").strip())
            age = int(input("What's your age? ").strip())
            sex = input("Select your sex:\nF for Femenine or M for Masculine: ")

            print("How much activity do you do? Select a number")
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
                get = act * (655 + (9.56 * weight) + (1.85 * height) - (4.7 * age))
                print(f"The calories you need are: {get:.2f} kcal")
                return get
            elif sex.casefold() == "m":
                match act:
                    case 1:
                        act = 1.6
                    case 2:
                        act = 1.78
                    case 3:
                        act = 2.1
                get = act * (66.4730 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age))
                print(f"The calories you need are: {get:.2f} kcal")
                return get
            else:
                pass
        except ValueError:
            print("Value is not valid")
            continue

# To get the calores and grams of carbs    
def cal(energy):
    while True:
        try:
            print("The previous result indicates how many calories you need to consume to stay as you are.")
            print("If you want to loose weight you can down your result, but not by more than 500 kcal")
            cals = float(input("How many calories would you like to consume daily? ").strip())

            if (cals >= (energy - 500)):
                print("Now, we need to define the percentages of carbs, proteins and fats.")
                print("The total sum of these porcentages should be: 100%")
                return cals
            else:
                print("Not enough calories")
                continue
        except ValueError:
            print("Value is not valid")
            continue
                
def carbs(cals):
    while True:
        try:
            print("Recommended carbohydrates %: 45-60%")
            carbs_per = float(input("Carbs %: ").strip().strip("%"))
            if carbs_per >= 45 and carbs_per <=60:
                carbs_cal = float(carbs_per * cals / 100)
                carbs_g = carbs_cal /4 
                print(f"You need {carbs_g:.2f} g")
                print(f"You still have {100 - carbs_per}% for proteins and lipids")
                carbs2 = (carbs_g, carbs_per)
                return carbs2
            else:
                print("You need to consume at least 45% and at much 60%")
                continue
        except ValueError:
            print("Value is not valid") 
            continue
                
def prot(cals, per1):
    while True:
        try:
            print("Recommended proteins %: 10-35%")
            prot_per = float(input("Proteins %: ").strip().strip("%"))
            if prot_per >= 10 and prot_per <=35:
                prot_cal = float(prot_per * cals / 100) 
                prot_g = prot_cal / 4                               
                print(f"You need {prot_g:.2f} g")
                print(f"You still have {100 - per1 - prot_per}% for lipids")
                prot2 = (prot_g, prot_per)
                return prot2
            else:
                print("You need to consume at least 10% and at much 35%")
                continue                    
        except ValueError:
            print("Value is not valid")
            continue

def fat(cals):
    while True:
        try:
            print("Recommended fats %: 20-35%")
            fat_per = float(input("Fats %: ").strip().strip("%"))
            if fat_per >= 20 and fat_per <=35:
                fat_cal = float(fat_per * cals / 100)
                fat_g = fat_cal / 4
                print(f"You need {fat_g:.2f} g")
                fat2 = (fat_g, fat_per)
                return fat2
            else:
                print("You need to consume at least 20% and at much 35%")
                continue
        except ValueError:
                print("Value is not valid")
                continue

def percent(carbs, prot, fat):
    if (carbs + prot + fat) == 100:
        return True
    else:
        return False




main()