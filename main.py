file_path = "passwords.txt"

password = input("Veuillez entrer votre mot de passe : ")
def write_password(file_path):
    fichier = open(file_path, "a")
    fichier.write(password)
    fichier.write("\n")
    fichier.close()

def open_file(file_path):
    fichier = open(file_path, "r")
    print(fichier.read())

def __main__():
    write_password(file_path)
    open_file(file_path)

__main__()