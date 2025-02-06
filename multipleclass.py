class multipleclass():
    def SubfieldsinAI(subfields):
        print("Sub-fields in AI are:",*subfields,sep="\n")
        return 
    def oddeven():
        number=int(input("Enter a number:"))
        if (number%2==0):
            print(number,"is a even number")
        else:
            print(number,"is a odd number")
        return 
    def eligible():
        gender=input("Your Gender:")
        age=int(input("Your age:"))
        if(gender=='Male' and age>=21):
            print("ELIGIBLE")
        elif(gender=='Female' and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
        return
    def percentage():
        s1=float(input("Subject1="))
        s2=float(input("Subject2="))
        s3=float(input("Subject3="))
        s4=float(input("Subject4="))
        s5=float(input("Subject5="))
        Total=s1+s2+s3+s4+s5
        percentage=(Total/500)*100
        print("Total:",Total)
        print("Percentage:",percentage)
        return
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area Formula:(Height*Breadth)/2")
        print("Area of Triangle:",(H*B)/2)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breadth:"))
        print("Perimeter Formula=Height1+Height2+Breadth")
        print("Perimeter of Triangle:",(h1+h2+b))
        return