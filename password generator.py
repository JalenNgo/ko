import random
import string

def validate_password_length(length):
    if length < 3:
        raise ValueError("Password length must be at least 3 to include a letter, number, and symbol.")

def get_characters():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    return letters, digits, symbols

def generate_password(length):
    validate_password_length(length) 
    
    letters, digits, symbols = get_characters()
    
    password = [
        random.choice(letters),  
        random.choice(digits),   
        random.choice(symbols)   
    ]
    
    characters = letters + digits + symbols
    password += random.choices(characters, k=length - 3)
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    length = int(input("How long should the password be? "))
    
    try:
        password = generate_password(length)
        print("Here is your password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
