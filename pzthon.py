
#  NEUPRAVOVAT
loop = 1
while loop == 1:

    vysledek=0

    num1=input("prvni cislo: ").replace(" ", "")
    oprt=input("operace: ").replace(" ", "")
    num2=input("druhe cislo: ").replace(" ", "")


    try:

        if num1=="π" or num1=="pi":
            num1=3.1415926535
        else:
            num1=float(num1)
        if num2=="π" or num2=="pi":
            num2=3.1415926535
        else:
            num2=float(num2)


# TVUJ KOD:

        if oprt=="+":
            vysledek=num1 + num2
        elif oprt=="-":
            vysledek=num1 - num2
        elif oprt=="*":
            vysledek=num1*num2
        elif oprt=="/":
            if int(num2)==0:
                print("Jsi hloupý 0 nelze dělit!!!")
            else:
                vysledek=num1 / num2
        else:
            print("Tato operace neexistuje!!")
        if int(vysledek)==vysledek:
            print(int(vysledek))
        else:
            print(vysledek)

    except:
        print("Syntax ERROR")
        break
