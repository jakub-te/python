#  NEUPRAVOVAT

num1=input("prvni cislo: ")
oprt=input("operace: ")
num2=input("druhe cislo: ")

# TVUJ KOD:
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