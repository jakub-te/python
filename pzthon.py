#  NEUPRAVOVAT
loop = 1
while loop == 1:

    num1=input("prvni cislo: ").replace(" ", "")
    oprt=input("operace: ").replace(" ", "")
    num2=input("druhe cislo: ").replace(" ", "")

    if not num1.isdigit() or not num2.isdigit():
        if num1.isalpha() or num2.isalpha():
            print("DEMENTALE / písmena nejsou čísla")
        else:    
            print("DEMENTALE / operatory nejsou čísla")
    else:

    # TVUJ KOD:
        if  num1.isnumeric() or num2.isnumeric():
            if num1=="" or num2=="":                         
                print("Napiš tam nějaké číslo!")
            elif oprt == "+" or  oprt == "-" or  oprt == "*" or  oprt == "/":
                if oprt=="+":
                    print(int(num1) + int(num2))
                elif oprt=="-":
                    print(int(num1) - int(num2))
                elif oprt=="*":
                    print(int(num1) * int(num2))
                elif oprt=="/":
                    if int(num2)==0:
                        print("Jsi hloupý 0 nelze dělit!!!")
                    else:
                        print(int(num1) / int(num2))
                else:
                    print("Tato operace neexistuje!!")
            else:
                print("Nesprávný operator.")
        else:   
            if num1=="" or num2=="": 
                print("Napiš tam nějaké číslo!")
            else:   
                print("Toto je kalkulačka, písmena bys zadávat neměl!")