

class Store:
    import os
    def menu(self):
        start = True
        f  = open("menu.txt","r")
        ascii = "".join(f.readlines())
        print(ascii)

        while start:
           inp = input("")
           if inp == "1":
               start = False

