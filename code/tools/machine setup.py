import sys
sys.path.append('path/to/src/')
from Database import Database as db

d = db()

g = 1
while g:
    n = input("enter name of machine(enter -1 to not change): ")
    try:
        if n == "-1":
            n = d.get_machineName()
        g = 0
    except:
        print("enter again!")
paass = input("Enter Password: ")
d.insert_data("3TpwcVKduP",
              n,
"""def decrypt(text):
    return 'Decrypted'""",
              paass,
              'Token'
             )