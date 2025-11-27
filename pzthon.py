
#  NEUPRAVOVAT
chyba = 0
while True:

    vysledek=0
    true1=True
    true2=True
    true3=True

    while true1:
        num1=input("prvni cislo: ").replace(" ", "").replace(",", ".")
        try:
            if num1=="π" or num1=="pi":
                num1=3.1415926535
            elif num1=="e":
                num1=2.7182818284
            else:
                num1=float(num1)
            true1=False
        except:
            print("Syntax ERROR\nZkus to znovu!")
            chyba+=1
            if chyba>=10:
                print("Radsi uz to nezkousej, STACILO!")
                break
    if chyba>=10:
        break
    while true2:
        num2=input("druhe cislo: ").replace(" ", "").replace(",", ".")
        try:
            if num2=="π" or num2=="pi":
                num2=3.1415926535
            elif num2=="e":
                num2=2.71828
            else:
                num2=float(num2)
            true2=False
        except:
            print("Syntax ERROR\nZkus to znovu!")
            chyba+=1
            if chyba>=10:
                print("Radsi uz to nezkousej, STACILO!")
                break
    if chyba>=10:
        break
    while true3:
        oprt=input("operace: ").replace(" ", "")
        if oprt=="+" or oprt=="-" or oprt=="*":
# TVUJ KOD:
            if oprt=="+":
                vysledek=num1 + num2
            if oprt=="-":
                vysledek=num1 - num2
            if oprt=="*":
                vysledek=num1*num2

            if int(vysledek)==vysledek:
                print(int(vysledek))
            if not int(vysledek)==vysledek:
                print(vysledek)
            true3=False
        elif oprt=="/" and not int(num2)==0:
            vysledek=num1 / num2
        else:
            print("Syntax ERROR\nZkus to znovu!")
            chyba+=1
            if chyba>=10:
                print("Radsi uz to nezkousej, STACILO!")
                break
    if chyba>=10:
        break
