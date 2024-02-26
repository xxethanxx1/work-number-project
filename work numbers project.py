import random
import string

def generate_unique_code(first_letter_name, first_letter_lastname, gender):
    if gender == 'M':
        random_number = random.randint(10, 50)
    elif gender == 'F':
        random_number = random.randint(51, 99)
    else:
        raise ValueError("Genre invalide. Veuillez entrer 'M' pour masculin ou 'F' pour féminin.")

    unique_code = f"{first_letter_name.upper()}{first_letter_lastname.upper()}{random_number}"
    return unique_code

def save_employee_info(full_name, unique_code):
    with open("employee_data.txt", "a") as file:
        file.write(f"{full_name},{len(full_name)},{unique_code}\n")

def check_employee_info(full_name, unique_code):
    try:
        with open("employee_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                stored_full_name, _, stored_unique_code = line.strip().split(',')
                if stored_full_name == full_name and stored_unique_code == unique_code:
                    return True
        return False
    except FileNotFoundError:
        return False

def main():
    new_employee = input("Êtes-vous un nouvel employé ? (oui/non): ").lower() == 'oui'

    if new_employee:
        try:
            first_name = input("Entrez votre prénom : ").strip()
            if not first_name.isalpha():
                raise ValueError("Prénom invalide. Veuillez entrer uniquement des caractères alphabétiques.")

            last_name = input("Entrez votre nom de famille : ").strip()
            if not last_name.isalpha():
                raise ValueError("Nom de famille invalide. Veuillez entrer uniquement des caractères alphabétiques.")

            gender = input("Entrez votre genre (M pour masculin, F pour féminin) : ").upper()
            if gender not in ['M', 'F']:
                raise ValueError("Genre invalide. Veuillez entrer 'M' pour masculin ou 'F' pour féminin.")
        except ValueError as e:
            print(f"Erreur : {e}")
            return

        full_name = f"{first_name} {last_name}"
        print("\n***************************")
        print("      Informations personnelles")
        print("***************************")
        print(f"\nNom complet : {full_name}")
        print(f"Longueur du nom complet : {len(full_name)}")

        first_letter_name = first_name[0]
        first_letter_lastname = last_name[0]
        unique_code = generate_unique_code(first_letter_name, first_letter_lastname, gender)
        print(f"Code unique : {unique_code}")

        save_employee_info(full_name, unique_code)
        print("Informations sur l'employé enregistrées avec succès.")

    else:
        full_name = input("Entrez votre nom complet : ").strip()
        unique_code = input("Entrez votre code unique : ").strip()

        if check_employee_info(full_name, unique_code):
            print("Informations sur l'employé trouvées. Bienvenue!")
        else:
            print("Erreur : Informations sur l'employé non trouvées. Veuillez vérifier vos coordonnées.")

if __name__ == "__main__":
    main()
