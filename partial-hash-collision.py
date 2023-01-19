import hashlib

pass_file = open('rockyou.txt', 'r', encoding="ISO-8859-1")
data = pass_file.read()
pass_list = data.split('\n')

for password in pass_list:
    hashed_pass = hashlib.md5(password.encode())
    if str(hashed_pass.hexdigest())[:3] == "9ed":
        print("Password = " + password)
        break

pass_file.close()
print("Finished")