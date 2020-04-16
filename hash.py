import bcrypt
password = test.encode('UTF-8')

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
if bcrypt.checkpw(password, hashed):
    print(hashed)

else:
    print("NOK")



