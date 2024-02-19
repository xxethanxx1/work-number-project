import random
import string

def generate_unique_code(first_letter_name, first_letter_lastname, gender):
    if gender == 'M':
        random_number = random.randint(10, 50)
    elif gender == 'F':
        random_number = random.randint(51, 99)
    else:
        raise ValueError("Invalid gender input. Please enter 'M' for male or 'F' for female.")

    unique_code = f"{first_letter_name.upper()}{first_letter_lastname.upper()}{random_number}"
    return unique_code

def main():
    try:
        first_name = input("Enter your first name: ").strip()
        if not first_name.isalpha():
            raise ValueError("Invalid first name. Please enter alphabetic characters only.")

        last_name = input("Enter your last name: ").strip()
        if not last_name.isalpha():
            raise ValueError("Invalid last name. Please enter alphabetic characters only.")

        gender = input("Enter your gender (M for man, F for female): ").upper()
        if gender not in ['M', 'F']:
            raise ValueError("Invalid gender input. Please enter 'M' for male or 'F' for female.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    
    print("\n***************************")
    print("      Personal Info")
    print("***************************")

    
    full_name = f"{first_name} {last_name}"
    print(f"\nFull Name: {full_name}")
    print(f"Length of Full Name: {len(full_name)}")

    
    first_letter_name = first_name[0]
    first_letter_lastname = last_name[0]
    unique_code = generate_unique_code(first_letter_name, first_letter_lastname, gender)
    print(f"Unique Code: {unique_code}")

if __name__ == "__main__":
    main()
