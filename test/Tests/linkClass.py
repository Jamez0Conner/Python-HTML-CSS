from inputFunction import mainloop
from numpy import *
from numpy import array
# Len,numpy, array, type casting, 
# input string to int,dictionary,string,list methods, 
class connector(mainloop):
    def runLink():
        iD = Identification
        while iD == True:
            Identification = "User2"
            phone_Number = input(int("Enter Phone Number:"))
            Email = input(int("Enter Email: "))
            if Identification == "User 1":
                print(Identification + "" + phone_Number + "" + Email)
            if Identification == "User2":
                print("Admin Rights Granted!" + "" + len(Identification, phone_Number, Email), + len(Email + Identification + phone_Number))
            else:
                quit()
            break   
    def funcs():    
        Var = 30
        Erb = 460
        while Erb == 40:
            if Var == 30:
                if Erb == 40:
                    print(Var + Erb)
                    continue
            else:
                if Var != 30:
                    if Erb != 40:
                        print("Not Applicable")
                        break
# while and for loops, in range, class and def, from and importing to connect two classes
# break, pass, if else statements, and print values
class typeCast():
    def cast():
            line_In = ["1,2,3,4"]
            Array = line_In
            array.__init__ = Array

            for i in range(len(Array)):
                print(Array[i])
    def Line():
        inLine = "1,3,5,7,9"
        arr= inLine
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        print(arr)







                
            

    