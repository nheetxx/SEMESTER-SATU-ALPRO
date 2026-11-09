weakPasswd = ("admin", "123456", "password", "root", "qwerty")

userData = {"username": input("Masukkan username: ")}

while True:
    userData["password"] = input("Masukkan password: ")
    print(f"Memeriksa akun: {userData['username']}...")

    if userData["password"] in weakPasswd:
        print("STATUS: Password Anda lemah.")
    elif userData["password"] == userData["username"]:
        print("STATUS: Password tidak boleh sama dengan username.")
    else:
        print("STATUS: Password cukup kuat.")
        break

print("Data akun:")
for i in userData:
    print(f"{i}: {userData[i]}")

print("Daftar password lemah:")
for i in weakPasswd:
    print(i, end=", ")
