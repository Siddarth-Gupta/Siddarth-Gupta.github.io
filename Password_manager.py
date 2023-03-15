#caeser cypher
pwd = "test"
masterPassword = input("enter masterpassword here: ")
numb = int(input("enter key number: "))
num = 5
def encode(password):
    str = password
    str_n = ""
    for ch in str: 
        ch_n = chr(ord(ch)+num)
        str_n += ch_n
    return str_n

def decode(pass_w):
    str = pass_w
    str_n = ""
    for ch in str:
        ch_n = chr(ord(ch)-numb)
        str_n += ch_n
    return str_n

def add():
    username = input("enter username: ")
    password = input("enter password: ")
    f1 = open("PasswordCollection.txt", "a")
    passw = encode(password)
    f1.write(f"{username} | {passw}\n")
    f1.close()

def view():
    f2 = open("PasswordCollection.txt", "r")
    for line in f2.readlines():
        data = line.rstrip()
        userN, passW = data.split(" | ")
        pass_W = decode(passW)
        print(f"Username = {userN} and Password = {pass_W}")
    f2.close()

if masterPassword == pwd:
    choice = int(input("Would u like to view the passwords(1) or add a new password(2)? "))
    if choice == 1:
        view()
    elif choice == 2:
        add()  
    else:
        print("error, wrong choice")