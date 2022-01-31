import colors

class Store:

    import os

    def menu(self):
        text_color = colors.ColorChanger()

        start = True
        f  = open("game_ascii/menu.txt","r")
        ascii = "".join(f.readlines())
        print(ascii)

        while start:
           inp = input("Enter:")
           if inp == "1":
               inp = input("To login enter 'log'. If new to the game enter 'new' to create an account. \n")
               if inp == "log" or "LOG" or "Log":
                  f = open("game_ascii/login_menu.txt")
                  ascii = "".join(f.readlines())
                  print(text_color.colorText(ascii))
                  print(text_color.colorText("[[white]]"))
                  inp = input("Username: ")
                  if inp == "m":
                      f = open("game_ascii/login_menu_pass.txt")
                      ascii = "".join(f.readlines())
                      print(text_color.colorText(ascii))
                      print(text_color.colorText("[[white]]"))
                      

                      inp = input("Password: ")
                      if inp == "p":
                          print(text_color.colorText("[[white]]LOGGED IN!"))

                          start = False
                          game_on = True

                          f = open("game_ascii/game_menu.txt")
                          ascii = "".join(f.readlines())
                          print(text_color.colorText(ascii))
                          print(text_color.colorText("[[white]]"))
                          while game_on:
                              game_on = False

           elif inp == "2":
                start = False
                print("QUIT GAME")

