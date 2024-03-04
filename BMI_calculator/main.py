height = float(input("enter height in meters: "))
weight = float(input("enter weight in kilograms: "))


def BMI(height, weight):
    bmi = weight / (height * height)
    if bmi < 16:
        return "severely underweight", bmi
    elif 16 <= bmi < 18.5:
        return "underweight", bmi
    elif 18.5 <= bmi < 25:
        return "normal", bmi
    elif 25 <= bmi < 30:
        return "overweight", bmi
    elif 30 <= bmi < 35:
        return "obese class I", bmi
    elif 35 <= bmi < 40:
        return "obese class II", bmi
    elif bmi >= 40:
        return "obese class III", bmi


quote, bmi = BMI(height, weight)
print('your bmi is: {} and you are: {}'.format(bmi, quote))
