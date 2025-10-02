file_path = "passwords.txt"

print("1 - Voir mes mots de passes \n" \
"2 - Crée un mot de passe \n" \
"3 - Modifier un mot de passe \n" \
"4 - Supprimer un mot de passe ")



def choice_usr():
    choice = int(input("Que souhaitez vous effectuer : "))
    while 1 < choice or choice > 4:
        choice = int(input("Que souhaitez vous effectuer : "))
        if choice == 1:
            open_file(file_path)
        elif choice == 2:
            write_password(file_path)
        elif choice == 3:
            edit_password(file_path)
        elif choice == 4:
            delete_password(file_path)

def write_password(file_path):
    password = input("Veuillez entrer votre mot de passe : ")
    fichier = open(file_path, "a")
    fichier.write(password)
    fichier.write("\n")
    fichier.close()

def open_file(file_path):
    fichier = open(file_path, "r")
    print(fichier.read())

def edit_password(file_path):
    fichier = open(file_path, "a")
    fichier.close()

def delete_password(file_path):
    fichier = open(file_path, "a")
    fichier.close()

def __main__():
    choice_usr()

__main__()