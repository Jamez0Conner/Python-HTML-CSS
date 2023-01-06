from linkClass import *

class Inputloop(typeCast):
    def InputVar():        
        Q = input("Test This Code! Does it work? (y/n)")
        if Q != "y":
                quit()
        else:
                print("Good work!")
class mainloop(Inputloop):
    def loop():
        run = True
        while run == True:
            Nums = [
                    1,2,3,4,5,
                    6,7,8,9,10,
                    11,12,13,14,
                    15,16,17,18
                    ]
            Char = ["A","B","C","D","E","F"]
            pairs = {
                1:"Option 1",
                2:"Option 2",
                3:"Option 3"
                }
            func = Char[0:5]
            method = pairs.get(2) and Nums.pop(3)
            Opp = [2,4,6,8,10]
            pass
            for i in Char:
                print(func)  
                print(Opp.reverse)
            else: 
                if run == False:
                    print(method)
                    print(pairs.values)
                    break
            break








