import os


file = open("wallet.txt","r")
wall = file.read()
wallet = wall.split()
count = len(wallet)


file2 = open("email.txt","r")
mail = file2.read()
email = mail.split()
count = len(wallet)

def copy():
    no = 0-1
    while True:
          no = no + 1
          aaaaa = input("Enter to copy : ")
          print(str(no)+". "+str(wallet[no]))
          print(str(no)+". "+str(email[no]))
          os.system("termux-clipboard-set "+wallet[no])
          os.system("termux-clipboard-set "+email[no])

copy()
