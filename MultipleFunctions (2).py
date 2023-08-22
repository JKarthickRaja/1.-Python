class multipleFunctions():

      def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
          print(temp)
      
      def OddEven():
        num=int(input("Enter a number: "))
        if((num%2)==1):
           print(num, "is odd number")
        else:
          print(num, "is even number")

      def Eligible():
        Gender=input("Your Gender: ")
        Age=int(input("Your Age: "))
        if(Gender=="Male"):
          if(Age>=21):
            print("Eligible")
          else:
            print("Not eligible")
        elif(Gender=="Female"):
          if(Age>=18):
            print("Eligible")
          else:
            print("Not eligible")

      def percentage():
        s1=int(input("Subject 1: "))
        s2=int(input("Subject 2: "))
        s3=int(input("Subject 3: "))
        s4=int(input("Subject 4: "))
        s5=int(input("Subject 5: "))
        Total=s1+s2+s3+s4+s5
        print("Total:", Total)
        Percentage=Total/500*100
        print("Percentage:", Percentage)

      def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        print("AreaFormula:(Height*Breadth)/2")
        print("Area of Triangle:", (Height*Breadth)/2)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        print("PerimeterFormula=Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Height1+Height2+Breadth)

      

          
              