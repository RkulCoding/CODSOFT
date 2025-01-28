import random
import string

def generate_password(length):
    """
    Generate a random password of specified length.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    if length < 1:
        return "Password length must be at least 1."
    
    # Define the character set: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters to generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Please enter a positive number for the password length.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
