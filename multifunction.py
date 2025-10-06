class multifunction():
    def bmi():
        bmi = float(input("Enter the BMI Index:"))
        if (bmi<18.5):
            print("Under Weight")
        
        elif (bmi<=24.9):
            print("Healthy Weight")
        
        elif (bmi<=29.9):
            print("Over Weight")
        
        elif (bmi<=34.9):
            print("Obese")
        
        elif (bmi<=39.9):
            print("Severly Obese")
        
        elif (bmi>=40):
            print("Morbidly Obese")

    def oddeven():
       
        Num = int(input("Enter the number: "))
        if (Num%2 ==1):
            print(Num, " is Odd number")            
        else:
            print(Num, " is Even number")

    def Elegible():
        Gender = input("Your Gender :")
        Age = int(input("Your Age :"))
        if (Gender == 'Male') and (Age >= 21):
            print("ELIGIBLE")
        elif (Gender == 'Female') and (Age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def Subfields():
        lists = ['Machine Learning', 'Neural Networks','Vision', 'Robotics','Speech Processing', 'Natural Language Processing' ]
        for i in lists:
            print(i)

    
    def percentage():
        Subject1 = int(input("Subject1= "))
        Subject2 = int(input("Subject2= "))
        Subject3 = int(input("Subject3= "))
        Subject4 = int(input("Subject4= "))
        Subject5 = int(input("Subject5= "))
        Total = (Subject1+Subject2+Subject3+Subject4+Subject5)
        print("Total : ", Total)
        Percentage = Total/5
        print("Percentage : ", Percentage)