#  NEUPRAVOVAT
loop = 1
while loop == 1:

    num1=input("prvni cislo: ").replace(" ", "")
    oprt=input("operace: ").replace(" ", "")
    num2=input("druhe cislo: ").replace(" ", "")

    if num1=="π" or num1=="pi":
        num1=3.1415926535
    else:
        num1=float(num1)
    if num2=="π" or num2=="pi":
        num2=3.1415926535
    else:
        num2=float(num2)
    if num1=="exit" or num2=="exit" or oprt=="exit":
        break

# TVUJ KOD:
    #if  num1.isnumeric() or num2.isnumeric():
    if oprt=="+":
        print(int(num1) + int(num2))
    elif oprt=="-":
        print(int(num1) - int(num2))
    elif oprt=="*":
        #print(int(num1) * int(num2))
        print(num1*num2)
    elif oprt=="/":
        if int(num2)==0:
            print("Jsi hloupý 0 nelze dělit!!!")
        else:
            print(int(num1) / int(num2))
    else:
        print("Tato operace neexistuje!!")
    # else:   
    #     print("Syntax ERROR")